from django.db import models

# Create your models here.
class Banda(models.Model):
    GENERO_CHOICES = [
        ('Alternativo', 'Alternativo'),
        ('Blues', 'Blues'),
        ('Glam Metal', 'Glam Metal'),
        ('Hard Rock', 'Hard Rock'),
        ('Heavy Metal', 'Heavy Metal'),
        ('Rock', 'Rock'),
        ('Metal', 'Metal'),
    ]

    nome = models.CharField('Nome', max_length=50)
    genero = models.CharField(max_length=50, choices=GENERO_CHOICES)
    integrantes = models.CharField('Integrantes', max_length=200)
    fundacao = models.DateField()