from django.db import models
from appprofile.models import Profile

class Message(models.Model):
	name = models.CharField(max_length=256)
	subject = models.CharField(max_length=256)
	message = models.TextField()
	flag = models.BooleanField(default=False)

	def __str__(self):
		return self.subject
