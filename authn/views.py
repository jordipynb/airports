from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from authn.models import UserRegisterForm
from django.contrib import messages
# from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['email']
            messages.success(request, f'Usuario {username} creado')
            return redirect('/')
    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, 'register.html', context)
