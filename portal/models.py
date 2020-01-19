from django.db import models
from django.utils import timezone
import PIL
from PIL import Image

# Create your models here.

class Noticia(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    
    foto = models.ImageField(upload_to='images/', null=True, blank=True)
    
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    data_criacao = models.DateTimeField(default=timezone.now)
    data_publicacao = models.DateTimeField(blank=True, null=True)

    def publicar(self):
        self.data_publicacao = timezone.now()
        self.save()
    def __str__(self):
        return self.titulo
        
class Area(models.Model):
    
    descricao = models.CharField(max_length=200)
    cor = models.CharField(max_length=200)
    status = models.BooleanField()

    def ativar(self):
        self.status = true
        self.save()
    def desativar(self):
        self.status = false
        self.save()
    
    def __str__(self):
        return self.descricao
        
