# forms.py dentro de tu aplicación donde está definido User

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        # Agrega aquí los campos que quieras mostrar en el formulario de registro
        fields = UserCreationForm.Meta.fields + ('email',)  # Ejemplo, añadir email
