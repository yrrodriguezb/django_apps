from django.urls import path
from .views import (
    LoginAppView,
    LogoutAppView,
    PasswordChangeAppView,
    PasswordChangeDoneAppView,
    PasswordResetAppView,
    PasswordResetDoneAppView,
    PasswordResetConfirmAppView,
    PasswordResetCompleteAppView
)


app_name = 'account'

urlpatterns = [
    path('login/', LoginAppView.as_view(), name='login'),
    path('logout/', LogoutAppView.as_view(), name='logout'),
    path('password_change/', PasswordChangeAppView.as_view(), name='password_change'),
    path('password_change/done/', PasswordChangeDoneAppView.as_view(), name='password_change_done'),
    path('password_reset/', PasswordResetAppView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneAppView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmAppView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteAppView.as_view(), name='password_reset_complete'),
]