from django.db import models

class App(models.Model):
	name = models.CharField(max_length=256, default='app1')
	log = models.CharField(max_length=256)
	link = models.URLField(blank=True)
	version = models.CharField(max_length=20, default='1.0')
	flag=models.BooleanField(default=False)

	def __str__(self):
		return self.name
