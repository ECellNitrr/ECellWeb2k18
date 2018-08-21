from django.db import models

class Mentor(models.Model):
    name = models.CharField(max_length=256)
    contact = models.TextField(max_length=13, null=True, blank=True)
    email = models.CharField(max_length=256)
    detail = models.TextField()
    description = models.TextField()
    profile_pic = models.ImageField(upload_to='static/uploads/mentors')
    flag = models.BooleanField(default=False)
    year = models.CharField(max_length=4, default=2018)

    def __str__(self):
        return self.name
