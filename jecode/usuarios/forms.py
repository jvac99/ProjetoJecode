from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UsuarioForm(UserCreationForm):
    email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'password1', 'password2']


'''
path('login/', auth_views.LoginView.as_view(
        template_name='usuarios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/', auth_views.PasswordChangeView, name='password_change'),
    path('password_change_done/', auth_views.PasswordChangeDoneView,
         name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView, name='password_reset'),
    path('cadastro/', views.cadastro, name='cadastro'),
'''