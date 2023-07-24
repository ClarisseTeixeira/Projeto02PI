from django.db import models

# Create your models here.

class Marca(models.Model):
    nome = models.CharField(max_length=250)
    def __str__(self):
        return self.nome 

class Produto(models.Model):
    nome = models.CharField(max_length=250)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='static/image')
    def __str__(self):
        return self.nome 


