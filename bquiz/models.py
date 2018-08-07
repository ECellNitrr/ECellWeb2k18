from django.db import models
from appprofile.models import Profile

class Questionset(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    set_no = models.IntegerField()
    meta = models.ImageField(upload_to='static/uploads/questionset')
    flag = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.name

class Question(models.Model):
    CHOICES = (
        ('IMG', 'Image Question'),
        ('TXT', 'Text Question')
    )
    question = models.CharField(max_length=256)
    description = models.TextField()
    meta = models.ImageField(upload_to='static/uploads/question', null=True, blank=True)
    time_limit = models.IntegerField()
    score = models.IntegerField()
    type = models.CharField(max_length=4, choices=CHOICES, default='TXT')
    set = models.ForeignKey(Questionset,on_delete=models.CASCADE)
    flag = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.question

class Answer(models.Model):
    question_id = models.ForeignKey(Question,on_delete=models.CASCADE)
    user_id = models.ForeignKey(Profile,on_delete=models.CASCADE)
    answer = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)

    def __int__(self):
        return self.answer

class QuestionAcknowledge(models.Model):
    acknowledge_id = models.IntegerField()
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return str(self.user.name + self.question.name)

class Option(models.Model):
    option = models.CharField(max_length=20, null=False, blank=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return str(str(self.question.question) + " => " + self.option)