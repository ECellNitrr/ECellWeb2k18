from django.db import models

# Create your models here.


class Event(models.Model):
	name = models.CharField(max_length=256)
	venue = models.TextField()
	date = models.DateField()
	time = models.CharField(max_length=10)
	details = models.TextField()
	cover_pic = models.ImageField(upload_to='static/uploads/events/cover')
	icon = models.ImageField(upload_to='static/uploads/events/icon')
	email = models.EmailField()
	flag = models.BooleanField(default=False)

	def __str__(self):
		return self.name