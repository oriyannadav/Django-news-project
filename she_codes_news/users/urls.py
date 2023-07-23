# users/urls.py
from django.urls import path
from .views import CreateAccountView, ChangeAccountView
from users.views import ResetPasswordView
from django.contrib.auth import views as auth_views
from . import views


app_name ='users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('change-account/', ChangeAccountView.as_view(), name='changeAccount'),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
        name='password_reset_confirm'),
    path('password-reset-complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
        name='password_reset_complete'),
    path('profile/', views.profile_view, name='userProfile'),
]