from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from .models import Post


from .models import Ejemplo

class EjemploForm(forms.ModelForm):
    class Meta:
        model = Ejemplo
        fields = ('nombre', 'email')



class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30)
    rut = forms.CharField(max_length=9)
    # Agrega otros campos adicionales aquí

    class Meta (UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'first_name','rut', 'password1', 'password2')


    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # Eliminar los mensajes de error de validaciones de contraseña
            for field_name in self.fields:
                field = self.fields.get(field_name)
                if field and field.widget.input_type == 'password':
                    field.widget.attrs.pop('autocomplete', None)
                    field.widget.attrs['placeholder'] = field.label
                    field.widget.attrs['class'] = 'form-control'

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['foto', 'titulo' ,'comentario']