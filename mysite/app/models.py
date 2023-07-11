from django.db import models
from django.contrib.auth.models import User


class Ejemplo(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nombre
    

class Post(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_Post = models.DateTimeField(auto_now_add=True)
    foto = models.ImageField(upload_to='post_photos/')
    titulo =    models.TextField()
    comentario = models.TextField()

    def __str__(self):
        return f"Post {self.id} - Autor: {self.autor.username}"
