
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm, UserRegistrationForm, UserEditForm

User = get_user_model()


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            print('ok')
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated Successfully')
                else:
                    return HttpResponse('Disabled Account')
            else:
                return HttpResponse('Invalid Login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(
            instance=request.user, data=request.POST, files=request.FILES)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error Updating messages')
    else:
        user_form = UserEditForm(instance=request.user)
    return render(request, 'account/edit.html', {'user_form': user_form})
