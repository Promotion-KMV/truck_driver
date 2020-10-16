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

	# model = Order
	# list_display = ['title', 'organization', 'adress_start', 
	# 				'adress_end', 'count', 'mass', 'price',
	# 				'data_publish', 'is_active', 'is_status',
	# ]
