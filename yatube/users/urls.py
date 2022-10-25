from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path(
        'signup/',
        views.SignUp.as_view(),
        name='signup'
    ),
    path(
        'login/',
        LoginView.as_view(template_name='users/login.html'),
        name='login'
    ),
    path(
        'logout/',
        LogoutView.as_view(template_name='users/logged_out.html'),
        name='logout'
    ),
    path(
        'password_reset_form',
        views.ChangePass.as_view(
            template_name='users/password_reset_form.html'
        ),
        name='password_reset_form'
    ),
    path(
        'password_reset_done',
        views.ChangePassEmail.as_view(
            template_name='users/password_reset_done.html'
        ),
        name='password_reset_done'
    ),
]
