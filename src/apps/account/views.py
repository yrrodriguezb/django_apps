from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import (
    LoginView, 
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile


class LoginAppView(LoginView):
    template_name = 'account/login.html'


class LogoutAppView(LogoutView):
    next_page = reverse_lazy('account:login')


class PasswordChangeAppView(PasswordChangeView):
    template_name = 'account/password_change.html'
    success_url = reverse_lazy('account:password_change_done')


class PasswordChangeDoneAppView(PasswordChangeDoneView):
    template_name = 'account/password_change_done.html'


class PasswordResetAppView(PasswordResetView):
    template_name = 'account/password_reset_form.html'
    email_template_name = 'account/password_reset_email.html'
    success_url = reverse_lazy('account:password_reset_done')


class PasswordResetDoneAppView(PasswordResetDoneView):
    template_name = 'account/password_reset_done.html'
    success_url = reverse_lazy('account:password_reset_confirm')


class PasswordResetConfirmAppView(PasswordResetConfirmView):
    template_name = 'account/password_reset_confirm.html'
    success_url = reverse_lazy('account:password_reset_complete')


class PasswordResetCompleteAppView(PasswordResetCompleteView):
    template_name = 'account/password_reset_complete.html'


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', { 'form': form })


def register(request):
    created_new_user = False
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            Profile.objects.create(user=new_user)
            created_new_user = True
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/signup.html', { 'form': user_form, 'created_new_user': created_new_user })


@login_required
def edit(request):
    modified_profile = False
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile, 
            data=request.POST, 
            files=request.FILES
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            modified_profile = True
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'account/edit.html', 
        { 'user_form': user_form, 'profile_form': profile_form, 'modified_profile' : modified_profile })