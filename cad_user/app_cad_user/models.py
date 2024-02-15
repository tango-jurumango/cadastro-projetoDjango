from django.db import models

# Create your models here.
    
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    idade = models.IntegerField()
    cpf = models.TextField(max_length=11, unique=True)
    email = models.CharField(max_length=300, unique=True)
    
