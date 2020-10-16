from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import *
from app_drivers import views
from django_email_verification import urls as mail_urls


app_name = "app_driver"

urlpatterns = [
    path('email/', include(mail_urls)),

#	path('',LoginView.as_view(template_name='base.html'), name='base'),
	path('', index, name='base'),
#	path('order/create', order_create, name='order_create'),
	path('oplata/<int:order_id>/', oplata, name='oplata'),
#	path('distance' )
#	path('order', OrderList.as_view(), name='order_list'),
	path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
	path('logout/', LogoutView.as_view(), name='logout'),
	path('register/', register, name='register'),
	path('create_data_mnfr/', create_data_manufacturer, name='create_data_manufacturer'),
	path('create_order/', create_order, name='create_order'),
	path('test_order/', test_order, name='test_order'),
	path('create_order_now/', create_order_now, name="create_order_now"),
	path('deferred_payment/', deferred_payment, name='deferred_payment'),
	path('my_order/', my_order, name='my_order'),
#	path('profile-create/', CreateUserProfile.as_view(),name='profile-create'),
]