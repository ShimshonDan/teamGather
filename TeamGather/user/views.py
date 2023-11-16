from django.shortcuts import render, redirect
from .models import User
from .forms import UsersForm
from django.core.exceptions import ValidationError

def login(request):
    return render(request, 'user\login.html')

def registartion(request):
    #add validation and hash password, email
    error=""
    if request.method == 'POST':
        form = UsersForm(request.POST)  
        try:
            if form.is_valid():
                form.save()
                return redirect('loginUser')
        except ValidationError:
            print(ValidationError.message)
            error = ValidationError.message
    
    form = UsersForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'user\\register.html', data)
