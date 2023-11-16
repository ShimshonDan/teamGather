from typing import Any
from .models import User
from django.forms import ModelForm, TextInput

class UsersForm(ModelForm):
    class Meta:
        model = User
        fields = ['login', 'email', 'numberPhone', 'password']

        widgets = {
            'login': TextInput(attrs={
                'class':'fill_login has_border_log', 
                'placeholder':'Логин'
            }), 
            'email': TextInput(attrs={
                'class':'fill_email has_border_mail', 
                'placeholder':'e-mail'
            }), 
            'numberPhone': TextInput(attrs={
                'class':'fill_telephone has_border_tel', 
                'placeholder':'Телефон'
            }), 
            'password': TextInput(attrs={
                'class':'fill_password has_border_pas', 
                'placeholder':'Пароль'
            })
        }