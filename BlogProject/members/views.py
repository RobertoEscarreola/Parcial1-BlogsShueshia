from audioop import reverse
from django.shortcuts import render
from django .views import generic
from django.urls import reverse_lazy
from .forms import SignUpForm, EditForm, PasswordChangingForm
from django.contrib.auth.views import PasswordChangeView

""" View de tipo CREATE para registrar usuario 
    Tomará como formulario la clase SignUpForm que es para logearse
    En el url tomará el nombre de registration/register.html
    Si el registro es satisfactorio redirigirá a home
"""
class UserRegister(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')



""" View de tipo UPDATE para actualizar la información del usuario 
    Tomará como formulario la clase EditForm que es para editar el usuario
    En el url tomará el nombre de registration/edit_profile.html
    Si el registro es satisfactorio redirigirá a home
"""
class UserEdit(generic.UpdateView):
    form_class = EditForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user



""" View de tipo PASSWORDCHANGE para cambiar la contraseña de usuario
    Tomará como formulario la clase PasswordChangingForm que es para cambiar la contraseña de usuario
    En el url tomará el nombre de registration/edit_profile.html
    Si el registro es satisfactorio redirigirá a password_success
"""
class PasswordsChange(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')

""" Función que detecta si el cambio de contraseña fue exitoso y te redirecciona """
def password_success(request):
    return render(request, 'registration/password_success.html', {})

""" NOTA: Por cada vista se hace un html """