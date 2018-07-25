from django.db import models

# Create your models here.

MEMBER_TYPE = (
        ('Dir', 'Director, NIT Raipur'),
        ('HCD', 'Head of Career development'),
        ('Fclty','Faculty Incharge'),
        ('MNG', 'Manager'),
        ('HC', 'Head Co-ordinator'),
        ('OC', 'Overall Co-ordinator'),
        ('EXEC', 'Executive'),
    )

class Member(models.Model):
	name = models.CharField(max_length=100)
	#designation = models.CharField(max_length=200)
	profile_url = models.URLField(blank=True, null=True)
	image = models.ImageField(upload_to='static/uploads/team', null=True, blank = True)
	member_type = models.CharField(max_length=5, choices= MEMBER_TYPE, default='EXEC')


	def __self__(self):
		return self.name