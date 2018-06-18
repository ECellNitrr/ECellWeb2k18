from django.db import models

# Create your models here.
class Speaker(models.Model):
	name = models.CharField(max_length=256)
	company = models.CharField(max_length=256)
	year = models.IntegerField()
	profile_pic = models.ImageField(upload_to='static/uploads/speakers')
	email = models.EmailField()
	contact = models.TextField(max_length=13, null=True, blank=True)
	flag = models.BooleanField(default=False)

	def __str__(self):
		return self.name
		