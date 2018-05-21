from django.db import models
from appprofile.models import Profile

class Message(models.Model):
	user = models.ForeignKey(Profile,on_delete=models.CASCADE)
	subject = models.CharField(max_length=256)
	message = models.TextField()
	flag = models.BooleanField()

	def __str__(self):
		return self.subject
