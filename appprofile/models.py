from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class WebMsg(models.Model):
    name = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    msg = models.TextField()

    def __str__(self):
        return self.name

# Profile Model
class Profile(models.Model):
    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
    
    USER_TYPE = (
        ('GST', 'Guest'),
        ('VLT', 'Voluteer'),
        ('EXE', 'Executive'),
        ('MNG', 'Manager'),
        ('HC', 'Head Co-ordinator'),
        ('OC', 'Overall Co-ordinator'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    linkedin = models.TextField(max_length=64, null=True, blank=True)
    facebook = models.TextField(max_length=64, null=True, blank=True)
    status = models.BooleanField(default=False)
    contact_no = models.TextField(max_length=12, null=True, blank=True, default='999999999')
    avatar = models.ImageField(upload_to='static/uploads/avatar', null=True, blank=True)
    user_type = models.CharField(
        max_length = 3,
        choices=USER_TYPE,
        default='GST'
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)
    #last_login = models.DateTimeField(auto_now=True, editable=False)
    otp = models.CharField(max_length=4, blank=True, null=True)


    def __str__(self):
        return str(self.user)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

