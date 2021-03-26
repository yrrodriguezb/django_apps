from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
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
from django.http.response import JsonResponse
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.views.decorators.http import require_POST
from apps.actions.models import Action
from apps.actions.utils import create_action
from common.decorators.http import ajax_required
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Contact, Profile


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
            create_action(new_user, 'has created an account')
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


@login_required
def user_list(request):
    users = User.objects.filter(is_active=True)
    return render(request, 'account/user/list.html', { 'users': users })


@login_required
def user_detail(request, username):
    user = get_object_or_404(User, username=username, is_active=True)
    return render(request, 'account/user/detail.html', { 'user': user })


@ajax_required
@require_POST
@login_required
def user_follow(request):
    from json import loads
    post_data = dict(loads(request.body.decode("utf-8")))
    user_id = post_data.get('id')
    action = post_data.get('action')
    if user_id and action:
        try:
            user = User.objects.get(id=user_id)
            if action == 'follow':
                Contact.objects.get_or_create(user_from=request.user, user_to=user)
                create_action(request.user, 'is following', user)
            else:
                Contact.objects.filter(user_from=request.user, user_to=user).delete()
            return JsonResponse({ 'code': 200, 'status': 'ok' })
        except User.DoesNotExist:
            return JsonResponse({ 'code': 500, 'status':'error' })
    return JsonResponse({ 'code': 500, 'status': 'error' })


@login_required
def dashboard(request):
    # Display all actions by default
    actions = Action.objects.exclude(user=request.user)
    following_ids = request.user.following.values_list('id', flat=True)
    
    if following_ids:
        # If user is following others, retrieve only their actions
        actions = actions.filter(user_id__in=following_ids)
    
    actions = actions\
        .select_related('user', 'user__profile')\
        .prefetch_related('target')[:10]

    return render(request,'account/activity.html', { 'actions': actions })