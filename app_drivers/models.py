from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import reverse
from django.utils import timezone
import uuid
from django.db import models
import datetime
import time
from .service import *


class UserProfile(models.Model):

	IP = 'IP'
	OOO = 'OOO'
	PD = 'PD'

	TYPE_ORGANIZATION = [
		(IP, 'ИП',),
		(OOO, 'ООО'),
		(PD, 'Частный перевозчик'),
	]

	REGIST_CUSTOMER = 'RC'
	REGIST_COMPANY_DRIVER = 'RCD'
	PRIVITE_DRIVER = 'PD'

	CHOICE_REGISTER = [
		(REGIST_CUSTOMER, 'Организация производитель'),
		(REGIST_COMPANY_DRIVER, 'Организация перевозчик'),
		(PRIVITE_DRIVER, 'Частный перевозчик')
	]

	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
	name = models.CharField(max_length=200, unique=True, verbose_name='название организации')
	type_organization = models.CharField(max_length=3, choices = TYPE_ORGANIZATION, verbose_name='Вид деятильности')
	email = models.EmailField (max_length = 254, verbose_name='Email организации')
	customer = models.CharField(max_length=3, choices=CHOICE_REGISTER, verbose_name='Вид деятельности'  )

	def __str__(self):
		return self.name
	

	@receiver(post_save, sender=User)
	def new_user(sender, instance, created, **kwargs):
		if created:
			UserProfile.objects.create(user=instance)
			instance.profile.save()

#Сохранение данных о Организации заказчика
class RegistCustomer(models.Model):
	MILK_PRODUCTION = 'MP'
	NON_ALCOHOLIC = 'NA'
	ALCOHOL_PRODUCTION = 'AP'
	OTHER = 'OH'

	ACTIVITY_ORGANIZATION = [
		(MILK_PRODUCTION, 'Молочная продукция'),
		(NON_ALCOHOLIC, 'безалкогольные напитки'),
		(ALCOHOL_PRODUCTION, 'алкогольная продукция'),
		(OTHER, 'другое'),
	]	
	title = models.ForeignKey(UserProfile,
							 on_delete=models.CASCADE,
							 verbose_name = 'Организация заказчик',
							)
	adress = models.CharField(max_length=300, verbose_name='Фактический адрес')
	phone = PhoneNumberField(max_length = 255, unique=True, verbose_name='Телефон для связи')
	activity = models.CharField(max_length=2, choices=ACTIVITY_ORGANIZATION, verbose_name='Сфера деятельности')
	other = models.CharField(max_length=300, verbose_name='название продукции', null=True, blank=True)
	image = models.ImageField(upload_to='media/%Y/%m/%d', null=True, blank=True)


	class Meta:
		verbose_name = 'Сведения о компании'
		verbose_name_plural = 'Сведения о компании'

#Сохранение данных организации исполнителя
class RegistCompDriver(models.Model):
	name = models.CharField(max_length=200, unique=True, verbose_name='Организация доставщик')
	first_name = models.CharField(max_length=200, verbose_name='Имя контактного лица')
	adress = models.CharField(max_length=300, verbose_name='Фактический адрес организации')
	email = models.EmailField (max_length = 254, verbose_name='Email организации')
	phone = PhoneNumberField(max_length = 255, unique=True,)
	rating = models.SmallIntegerField(verbose_name='Рейтинг надежности компании')
	count = models.SmallIntegerField(verbose_name='Кол-во выполненных перевозок')

	def __str__(self):
		return self.name

# Сохранение данных о заказе
class Order(models.Model):
	REFRIJERAOTR = 'RFJR'
	FOOD_TANK = 'FDTK'
	ISOTERM = 'ISTM'
	TRUCK_VAN = 'TKVN'

	CAR_CASE = [
		(REFRIJERAOTR, 'РЕФРЕЖЕРАТОР',),
		(FOOD_TANK, 'ПИЩЕВАЯ ЦИСТЕРНА'),
		(ISOTERM, 'ИЗОТЕРМ'),
		(TRUCK_VAN, 'ФУРГОН'),
	]

	name = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	number_order = models.CharField(max_length=14, verbose_name='Номер заказа', default=1)
	title = models.CharField(max_length=200, verbose_name='Что перевозить',blank=False, null=False)
	citi_start = models.CharField(max_length=50, verbose_name='Откуда', )
	citi_end = models.CharField(max_length=50, verbose_name='Куда')
	adress_start = models.CharField(max_length=300, verbose_name='адрес отправки')
	adress_end = models.CharField(max_length=300, verbose_name='адрес доставки')
	email_sestination = models.EmailField (max_length = 254, verbose_name='Email организации')
	count = models.SmallIntegerField(verbose_name='Требуемое кол-во машин', default=1)
	mass = models.SmallIntegerField(verbose_name='Требуемая грузоподъемность')
	price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='цена', help_text='цена за 1 машину')
	price_on_kilo = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='цена за киллометр')
	distance = models.SmallIntegerField(verbose_name='Расстояние')
	time_in_distance = models.CharField(max_length=50, verbose_name='Время в пути')
	type_carcase = models.CharField(max_length=4, choices=CAR_CASE, verbose_name='Тип кузова')
	data_publish = models.DateTimeField(default=timezone.now, verbose_name='дата и время транспортировки')
	description = models.TextField(verbose_name='Коментарии', null=True, blank=True )
	is_active = models.BooleanField(verbose_name='опубликовать заказ', default=False)
	is_status = models.BooleanField(verbose_name='статус заказа', default=False)
	is_finish = models.BooleanField(verbose_name='заказ доставлен', default=False)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Заказ'
		verbose_name_plural = 'Заказы' 


#Регистрация водителей
# class RegistDriver(models.Model):
# 	nick_name = models.CharField(max_length=50, unique=True, verbose_name='Имя')
# 	first_name = models.CharField(max_length=50, verbose_name='Имя')
# 	last_name = models.CharField(max_length=50, verbose_name='Фамилия')
# 	email = models.EmailField (max_length = 254, verbose_name='Email')
# 	phone = PhoneNumberField(max_length = 12, unique=True, verbose_name='Телефон')
# 	birth_date = models.DateField(default=timezone.now, verbose_name='Дата рождения')
# 	rating = models.SmallIntegerField(verbose_name='Рейтинг надежности')
# 	count = models.SmallIntegerField(verbose_name='Кол-во выполненных перевозок')


# 	def __str__(self):
# 		return self.first_name


# Регистрация Транспорного средства
# class RegistrCar(models.Model):
	
# 	title_company = models.ForeignKey(RegistCompDriver, on_delete=models.CASCADE, verbose_name='Организация')
# 	title_driver = models.ForeignKey(RegistDriver, on_delete=models.CASCADE, verbose_name='Название опроса')
# 	brand = models.CharField(max_length=20, verbose_name='Марка ТС')
# 	model = models.CharField(max_length=20, verbose_name='Модель ТС')
# 	release_date = models.DateField(default=timezone.now, verbose_name='Год выпуска')
# 	register_sign = models.CharField(max_length=9, verbose_name='Регистрационный знак')
# 	passport_ts = models.IntegerField(verbose_name='номер паспорта тс')
# 	lifting_capacity = models.SmallIntegerField(verbose_name='Грузоподъемность')
# 	images = models.ImageField(upload_to='media/%Y/%m/%d',)

# 	def __str__(self):
# 		return self.brand


