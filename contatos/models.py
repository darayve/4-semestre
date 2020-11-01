from django.db import models

# Create your models here.

class Contato(models.Model):
  nome = models.CharField(max_length=100)
  endereco = models.TextField()
  celular = models.CharField(max_length=12)
  email = models.EmailField(max_length=254)
  data_nascimento = models.DateField()
  sexo = models.CharField(max_length=1)