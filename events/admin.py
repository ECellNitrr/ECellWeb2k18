from django.contrib import admin
from .models import Event, Cart, EventOrder

class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'venue', 'date','time')
    search_fields = ('id', 'name','venue','date', 'time')



class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    #search_fields = ('id', 'name','venue','date', 'time')


class EventOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart','event')

admin.site.register(Event, EventAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(EventOrder,EventOrderAdmin)
