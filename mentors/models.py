from django.db import models

class Mentor(models.Model):
    name = models.CharField(max_length=256)
    contact = models.TextField(max_length=13, null=True, blank=True)
    email = models.CharField(max_length=256)
    detail = models.TextField()
    description = models.TextField()
    profile_pic = models.ImageField(upload_to='Mentors')
    flag = models.BooleanField(default=False)

    def __str__(self):
        return self.name
