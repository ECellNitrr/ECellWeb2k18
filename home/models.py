from django.db import models

# Create your models here.

class Msg(models.Model):
    name = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    msg = models.TextField()

    def __str__(self):
        return self.name