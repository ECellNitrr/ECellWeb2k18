from django.db import models

# Create your models here.
class Sponsor(models.Model):
	name = models.CharField(max_length=256)
	details = models.TextField()
	pic = models.ImageField(upload_to='Sponsors')
	contact = models.TextField(max_length=13, null=True, blank=True)
	website = models.URLField(blank=True)
	spons_type = models.TextField()
	flag = models.BooleanField(default=False)

	def __str__(self):
		return self.name


