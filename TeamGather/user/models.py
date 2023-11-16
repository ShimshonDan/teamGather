from django.db import models
from django.core.validators import (
    EmailValidator, 
    MaxLengthValidator, MinLengthValidator, 
    ValidationError
)

from django.contrib.auth import password_validation

def clean_login(login: str):
    login = login.strip()
    if login.isspace():
        raise ValidationError('Логин не может состоять из пустой строки')

def clean_numberPhone(numberPhone):
    if len(numberPhone) > 12 and len(numberPhone) < 10:
        raise ValidationError('Неверно указан номер')

    try:
        firtsPart, secondPart = numberPhone.split('9')
        if (firtsPart) not in ['+7', '7', '8',]:
            return ValidationError('Неверно указан номер')
    except:
        secondPart = '9'+numberPhone
        if not secondPart.isdigit():
            return ValidationError('Неверно указан номер')



class User(models.Model):
    login = models.CharField('Login', max_length=50, null=False, validators=[
        MaxLengthValidator(
            limit_value=50, 
            message = 'Максимальная длина логина 50 символов!' 
        ), 
        MinLengthValidator(
            limit_value=5, 
            message = 'Минимальная длина логина 5 символов!' 
        ), 
        clean_login
    ]) 

    email =  models.EmailField('e-mail', max_length=50, null=False, validators=[EmailValidator(
        message= "Не корректный адрес электронной почты!")])

    numberPhone = models.CharField('Number phone', null=False, max_length=12, validators=[
        clean_numberPhone
    ])
    password = models.CharField('Password', null=False, max_length=50)

    def __str__(self) -> str:
        return self.login + " " + self.email + " "+ self.numberPhone + " "+self.password 
    

#TextField() - безразмерный текст - Резюме