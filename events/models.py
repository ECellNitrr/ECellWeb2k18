from django.db import models
from django.contrib.auth.models import User
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



class Cart(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	active = models.BooleanField(default=True)

	def add_to_cart(self, event_id):
		event = Event.objects.get(pk=event_id)
		
		new_order = EventOrder.objects.create(
			event=event,
			cart=self,
			quantity=1,
		)
		new_order.save()

	def remove_from_cart(self, event_id):
		event=Event.objects.get(pk=event_id)

		try:
			preexisting_order = EventOrder.objects.get(event=event, cart=self)

			
			preexisting_order.delete()

		except EventOrder.DoesNotExist:
			pass
			


class EventOrder(models.Model):
	event = models.ForeignKey(Event, on_delete=models.CASCADE)
	cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
	quantity = models.IntegerField()