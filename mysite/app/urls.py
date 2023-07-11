from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from .import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('',views.inicio, name ='index'),
    path('index', views.inicio, name='inicio'),
    path('login', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='inicio'), name='logout'),
    path('registro', views.register_view, name='registro'),
    

    path('tipos_te', views.tipo_te, name="tipos_te") ,
    path('pokedex', views.pokedex, name="pokedex"),
    path('tipos_te/te_boldo', views.te_boldo, name="te_boldo"),
    path('tipos_te/te_jazmin', views.te_jazmin, name="te_jazmin"),
    path('tipos_te/te_margarita', views.te_margarita, name="te_margarita"),
    path('tipos_te/te_pasiflora', views.te_pasiflora, name="te_pasiflora"),


    path('post/', views.listar_post, name='listar'),

    # Ruta para crear una nueva publicación
    path('Post/agregar', views.agregar_post, name='agregar'),

    # Ruta para editar una publicación existente
    path('Post/<int:post_id>/editar', views.editar_post, name='editar'),

    # Ruta para eliminar una publicación existente
    path('Post/<int:post_id>/borrar', views.borrar_post, name='borrar'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
