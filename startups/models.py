from django.db import models

# Create your models here.
class Startup(models.Model):
	name = models.CharField(max_length=256)
	email = models.CharField(max_length=256)
	pic = models.ImageField(upload_to='static/uploads/startups')
	contact = models.TextField(max_length=13, null=True, blank=True)
	founder = models.CharField(max_length=256)
	address = models.TextField()
	flag = models.BooleanField(default=False)

	def __str__(self):
		return self.name
