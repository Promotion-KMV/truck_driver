# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from app_drivers.models import UserProfile
from django.contrib.auth.backends import ModelBackend

UserModel = get_user_model()

class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, email=None, **kwargs):
        if '@' in username:
            kwargs = {'email': username}
        else:
            kwargs = {'username': username}

        try:
            user = UserModel.objects.get(email__iexact=username)
            if user.check_password(password):
                return user
            else:
                return None
        except User.DoesNotExist:
            return None
