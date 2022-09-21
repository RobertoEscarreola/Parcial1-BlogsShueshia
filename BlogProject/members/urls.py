from django.urls import path
from .views import UserRegister, UserEdit, PasswordsChange
from django.contrib.auth import views as auth_views
from . import views

""" URLS propias de esta aplicación miembros """
urlpatterns = [
    path('register/', UserRegister.as_view(), name='register'),
    path('edit_profile/', UserEdit.as_view(), name='edit_profile'),
    path('password/', PasswordsChange.as_view(template_name='registration/change-password.html')),
    path('password_success', views.password_success, name="password_success"),
]

""" NOTA: los path se usan para asignar un nombre a una dirección url """