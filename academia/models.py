from django.db import models

# Create your models here.
class Formacao(models.Model):
    nome = models.CharField(max_length=100)
    decricao = models.TextField(max_length=500)

    def __str__(self):
        return self.nome
    
class Instituicao (models.Model):
    nome = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nome} ({self.cidade})'
    
class Instrutor (models.Model):
    nome = models.CharField(max_length=100)
    email= models.EmailField(max_length=1000)
    data_nacimento= models.DateField(blank=True, null=True)


    def __str__(self):
        return f'{self.nome} ({self.data_nacimento})'
    
    