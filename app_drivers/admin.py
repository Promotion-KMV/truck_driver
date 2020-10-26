from django.contrib import admin

from app_drivers.models import *

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	model = Order
	list_display = ['name','title', 'is_active', 'is_status', 'id']

@admin.register(RegistCustomer)
class RegistCustomerAdmin(admin.ModelAdmin):
	model = RegistCustomer
	list_display = ['title', 'adress']


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
	pass

@admin.register(RegistCompDriver)
class RegistCompDriverAdmin(admin.ModelAdmin):
	model = RegistCompDriver
	list_display = ['title', 'adress']
