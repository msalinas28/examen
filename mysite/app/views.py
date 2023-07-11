from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import sweetify

from .forms import EjemploForm

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Post
from .forms import PostForm




#-------------------------------- redirecciones de paginas --------------------------------

def home_view(request):
    return redirect('inicio')


def inicio(request):
    return render(request, 'app/index.html')

def tipo_te(request):
    return render(request, 'app/tes_ext.html')

def pokedex(request):
    return render(request, 'app/pokedex_ext.html')

def te_boldo(request):
    return render(request, 'app/te_boldo.html')

def te_jazmin(request):
    return render (request,'app/te_jazmin.html')

def te_margarita(request):
    return render (request,'app/te_margarita.html')

def te_pasiflora(request):
    return render (request,'app/te_pasiflora.html')


#-------------------------------- ejemplo de form--------------------------------
# def ejemplo_view(request):
#     if request.method == 'POST':
#         form = EjemploForm(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form = EjemploForm()
#     return render(request, 'app/inicio.html', {'form': form})



#-------------------------------- Registrarse --------------------------------
def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  
    else:
        form = RegistrationForm()
    return render(request, 'app/registro.html', {'form': form})


#-------------------------------- Login --------------------------------
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('inicio') 
            else:
                error_message = 'Credenciales inválidas'
    else:
        form = LoginForm()
        error_message = None
    return render(request, 'app/login.html', {'form': form, 'error_message': error_message})

#-------------------------------- logout --------------------------------
def logout_view(request):
    logout(request)
    return redirect('inicio')


#-------------------------------- Sweet alert --------------------------------


def my_view(request):
    sweetify.warning(request, 'This is a warning... I guess')

#-------------------------------- Post --------------------------------

def listar_post(request):
    posts = Post.objects.all()
    return render(request, "post/postListar.html", {'posts': posts})



#agregar crud
@login_required
def agregar_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            messages.success(request, '¡Su post ha sido creado!')
            return redirect('listar')
        else:
            messages.error(request, 'Error, no se pudo subir su post')
    else:
        form = PostForm()
    return render(request, 'post/postAgregar.html', {'form': form})






#Borra crud


def borrar_post(request, post_id):
    instancia = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        instancia.delete()  
        return redirect('listar')
    return render(request, 'post/postBorrar.html', {'post': instancia})  







#editar crud

def editar_post(request, post_id):
    instancia = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=instancia)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Post editado correctamente!')
            return redirect('listar')
        else:
            messages.error(request, "Error, No se pudo editar su post")
    else:
        form = PostForm(instance=instancia)
    return render(request, "post/postEditar.html", {'form': form})


