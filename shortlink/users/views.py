from django.shortcuts import render, redirect
from rest_framework import request

from .serializers import UserSerializer
from django.contrib.auth.models import User

from .forms import UserRegisterForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile
from rest_framework.viewsets import ModelViewSet


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Пользовать {username} был успешно создан!')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(
        request,
        'users/registration.html',
        {
            'title': 'Страница регистрации',
            'form': form
        }
    )


@login_required
def profile(request):
    if request.method == "POST":

        updateUserForm = UserUpdateForm(request.POST, instance=request.user)

        if updateUserForm.is_valid():
            updateUserForm.save()
            messages.success(request, f'Ваш аккаунт был успешно обновлен!')
            return redirect('profile')

    else:

        updateUserForm = UserUpdateForm(instance=request.user)

    data = {
        'updateUserForm': updateUserForm
    }

    return render(request, 'users/profile.html', data)


