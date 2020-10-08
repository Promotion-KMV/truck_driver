# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404, loader
#from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import login, authenticate  
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import FormView, CreateView, ListView
from django.contrib.auth.forms import UserCreationForm
from django.forms import modelformset_factory, formset_factory
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib import messages
from django.urls import reverse_lazy
from django_email_verification import sendConfirm
from app_drivers.forms import *

from app_drivers.models import *
import time
from .service import *


def register(request):
    template = loader.get_template('base.html')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        email = request.POST.get('email')
        name = request.POST.get('name')
        customer = request.POST.get('customer')
        if UserProfile.objects.filter(email=email).exists():
            return HttpResponse('Пользователь с таким адресом электронной почты уже существует')
        if form.is_valid():
            user = form.save()                
            user.save()
#            user.refresh_from_db()#ошибка
            user.profile.email = form.cleaned_data.get('email')
            user.profile.name = form.cleaned_data.get('name')
            user.profile.customer = form.cleaned_data.get('customer')
            user.profile.save()
            sendConfirm(user)
#            user = authenticate(username=user.username, password=my_password, email=email)
#            my_password = form.cleaned_data.get('password1')
#            login(request, user) #ошибка
            return HttpResponseRedirect('http://yandex.ru/')

            #return render(request, 'base.html')
    else:
        form = SignUpForm()
        return render(request, 'register.html', context={'form': form})


def test_order(request):
    template = loader.get_template('base.html')
    data = {}

    return HttpResponse(template.render(data))


def create_data_manufacturer(request):
#    template = loader.get_template('create_data/create_data_manufacturer.html')
    RegistCustomerForm = modelformset_factory(RegistCustomer, fields=('adress', 'phone', 'activity', 'type_organization', 'other'))
    if request.method == 'POST':
        RegistCustomer.objects.all().create(title=UserProfile.objects.get(user=request.user),
#            name=UserProfile.objects.get(user=request.user).name,
            adress= request.POST['form-0-adress'],
            phone=request.POST['form-0-phone'],
            activity=request.POST['form-0-activity'],
            type_organization=request.POST['form-0-type_organization'],
            other=request.POST['form-0-other'],
        )
        return HttpResponse('ok')
    else:
        form = RegistCustomerForm(queryset=RegistCustomer.objects.none())
    return render(request, 'create_data/create_data_manufacturer.html', { 'form': form})




def index(request):
    template = loader.get_template('base.html')
    usersis = UserProfile.objects.get(user=request.user)
  


    data ={
        'usersis': usersis,


    }

    return HttpResponse(template.render(data, request))

    #return render(request, 'base.html')


def create_order(request):
    template = loader.get_template('base.html')
    OrderFormSet = modelformset_factory(Order, fields=('title',
                  'citi_start', 'citi_end', 'adress_start','adress_end', 'price',
                  'price_on_kilo', 'distance','time_in_distance', 'email_sestination', 'type_carcase',
                  'count', 'mass', 'data_publish', 'description'))

#            return HttpResponseRedirect(reverse_lazy('app_drivers:oplata', args=(Order.objects.last().id,))) 


    form = OrderFormSet(queryset=Order.objects.none())

    return render(request, 'create_data/create_order.html', {'form' : form}) 


def oplata(request):
    template = loader.get_template('oplate.html')
    order = Order.objects.all()
    data = {
        'order': order,
    }
    return HttpResponse(template.render(data, requests))
#Необходима валидация на заполнение данных
@csrf_exempt
def create_order_now(request):
    template = loader.get_template('oplate.html')
    a = random_number_order()
    if request.method == 'POST':

        Order.objects.all().create(name = UserProfile.objects.get(user=request.user),
            title = request.POST['form-0-title'],                
            number_order = 100,
#            organization = UserProfile.objects.get(user=request.user),
            adress_start = request.POST['form-0-adress_start'],
            adress_end = request.POST['form-0-adress_end'],
            citi_start = request.POST['form-0-citi_start'],
            citi_end = request.POST['form-0-citi_end'],
            email_sestination = request.POST['form-0-email_sestination'],
            count = request.POST['form-0-count'],
            mass = request.POST['form-0-mass'],
            price = request.POST['form-0-price'],
            price_on_kilo = request.POST['form-0-price_on_kilo'],
            distance = request.POST['form-0-distance'],
            time_in_distance =request.POST['form-0-time_in_distance'],
            description = request.POST['form-0-description'],
            type_carcase = request.POST['form-0-type_carcase'],
            )
        data = {}
        return HttpResponse(template.render(data))
            #return HttpResponseRedirect(reverse_lazy('app_drivers:oplata', args=(Order.objects.last().id,)))  
        # except:
        #    pass
        #    return HttpResponse('no ok')




# class OrderList(ListView):
#     model = Order
#     template_name = 'order_list.html'


def base(request):
    context = {}
    
    if request.user.is_authenticated:
        context['username'] = request.user.username

    return render(request, 'base.html', context)


#Реализовать форму добавления компании для размещения заказа
#Реализовать форму добавления заказа