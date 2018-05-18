from django.db import models
from appprofile.models import Profile
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

# Tasks Model
class Task(models.Model):
    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
    
    STATUSES = (
        ('to-do', 'To Do'),
        ('in-progress', 'In Progress'),
        ('blocked', 'Blocked'),
        ('done', 'Done'),
        ('dismissed', 'Dismissed')
    )
    PRIORITIES = (
        ('low', 'Low'),
        ('normal', 'Normal'),
        ('high', 'High'),
        ('critical', 'Critical'),
        ('blocker', 'Blocker')
    )
    title = models.CharField(_("title"), max_length=200)
    description = models.TextField(max_length=2000, null=True, blank=True)
    deadline = models.DateTimeField()
    assigned_to = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name='assignedto')
    assigned_by = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name='assignedby')
    state = models.CharField(max_length=20, choices=STATUSES, default='to-do')
    priority = models.CharField(max_length=20, choices=PRIORITIES, default='normal')
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return "[%s] to [%s] with priority [%s] on [%s]" % (str(self.assigned_by), str(self.assigned_to), self.priority, self.created_at.date())

# Checklist for a task
class CheckList(models.Model):
    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = "Check List"
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    is_done = models.BooleanField(default=False)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.description

def get_priority_point(user_type):
    priority = {}
    priority['GST'] = 0
    priority['VLT'] = 0
    priority['EXE'] = 1
    priority['MNG'] = 2
    priority['HC'] = 3
    priority['OC'] = 4
    return priority.get(user_type, -1)

@receiver(pre_save, sender=Task)
def check_hierarchy(sender, instance, *args, **kwargs):
    if(get_priority_point(instance.assigned_by.user_type) <= get_priority_point(instance.assigned_to.user_type)):
        raise Exception('Not enough privilege')