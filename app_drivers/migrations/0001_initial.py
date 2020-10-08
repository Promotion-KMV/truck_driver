# Generated by Django 3.1.1 on 2020-10-06 17:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistCompDriver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Организация доставщик')),
                ('first_name', models.CharField(max_length=200, verbose_name='Имя контактного лица')),
                ('adress', models.CharField(max_length=300, verbose_name='Фактический адрес организации')),
                ('email', models.EmailField(max_length=254, verbose_name='Email организации')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=255, region=None, unique=True)),
                ('rating', models.SmallIntegerField(verbose_name='Рейтинг надежности компании')),
                ('count', models.SmallIntegerField(verbose_name='Кол-во выполненных перевозок')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='название организации')),
                ('email', models.EmailField(max_length=254, verbose_name='Email организации')),
                ('customer', models.CharField(choices=[('RC', 'Организация производитель'), ('RCD', 'Организация перевозчик')], max_length=3, verbose_name='Вид деятельности')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RegistCustomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adress', models.CharField(max_length=300, verbose_name='Фактический адрес')),
                ('type_organization', models.CharField(choices=[('IP', 'ИП'), ('OOO', 'ООО')], max_length=3, verbose_name='Вид деятильности')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=255, region=None, unique=True, verbose_name='Телефон для связи')),
                ('activity', models.CharField(choices=[('MP', 'Молочная продукция'), ('NA', 'безалкогольные напитки'), ('AP', 'алкогольная продукция'), ('OH', 'другое')], max_length=2, verbose_name='Сфера деятельности')),
                ('other', models.CharField(blank=True, max_length=300, null=True, verbose_name='название продукции')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/%Y/%m/%d')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_drivers.userprofile', verbose_name='Организация заказчик')),
            ],
            options={
                'verbose_name': 'Сведения о компании',
                'verbose_name_plural': 'Сведения о компании',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_order', models.CharField(default=1, max_length=14, verbose_name='Номер заказа')),
                ('title', models.CharField(max_length=200, verbose_name='Что перевозить')),
                ('citi_start', models.CharField(max_length=50, verbose_name='Откуда')),
                ('citi_end', models.CharField(max_length=50, verbose_name='Куда')),
                ('adress_start', models.CharField(max_length=300, verbose_name='адрес отправки')),
                ('adress_end', models.CharField(max_length=300, verbose_name='адрес доставки')),
                ('email_sestination', models.EmailField(max_length=254, verbose_name='Email организации')),
                ('count', models.SmallIntegerField(default=1, verbose_name='Требуемое кол-во машин')),
                ('mass', models.SmallIntegerField(verbose_name='Требуемая грузоподъемность')),
                ('price', models.DecimalField(decimal_places=2, help_text='цена за 1 машину', max_digits=8, verbose_name='цена')),
                ('price_on_kilo', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='цена за киллометр')),
                ('distance', models.SmallIntegerField(verbose_name='Расстояние')),
                ('time_in_distance', models.CharField(max_length=50, verbose_name='Время в пути')),
                ('type_carcase', models.CharField(choices=[('RFJR', 'РЕФРЕЖЕРАТОР'), ('FDTK', 'ПИЩЕВАЯ ЦИСТЕРНА'), ('ISTM', 'ИЗОТЕРМ'), ('TKVN', 'ФУРГОН')], max_length=4, verbose_name='Тип кузова')),
                ('data_publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='дата и время транспортировки')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Коментарии')),
                ('is_active', models.BooleanField(default=False, verbose_name='опубликовать заказ')),
                ('is_status', models.BooleanField(default=False, verbose_name='статус заказа')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_drivers.userprofile')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]