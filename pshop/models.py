from http import client
from django.db import models

      
class Cliente(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    telefone = models.CharField(max_length=14, null=False, blank=False)
    CPF = models.CharField(max_length=14, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    rua = models.CharField(max_length=200, null=False, blank=False)
    numero = models.IntegerField(null=False, blank=False)
    bairro = models.CharField(max_length=50, null=False, blank=False)
    cidade = models.CharField(max_length=100, null=False, blank=False)
    pais = models.CharField(max_length=50, null=False, blank=False)


    def __str__(self):
        return self.nome


class Pet(models.Model):
    SEXO_CHOICES = (
        ("F", "Fêmea"),
        ("M", "Macho"),
        ("N", "Outro")
    )

    PORTE_CHOICES = (
        ("p", "Pequeno"),
        ("M", "Médio"),
        ("G", "Grande"),
        ("N", "Outro")
    )

    TIPO_CHOICES = (
        ("Gato", "Gato(a)"),
        ("Cachorro", "Cachorro(a)"),
        ("Outro", "Outro")
    )

    nome = models.CharField(max_length=100, null=False, blank=False)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=False, null=False)
    raca = models.CharField(max_length=20, null=False, blank=False)
    porte = models.CharField(max_length=1, choices=PORTE_CHOICES, blank=False, null=False)
    idade = models.IntegerField(null=False, blank=False)
    tipo = models.CharField(max_length=11, choices=TIPO_CHOICES, blank=False, null=False)

    
    def __str__(self):
        return self.nome



class Servico(models.Model):
    PAG_CHOICES = (
        ("Dinheiro", "Dinheiro"),
        ("Cartao", "Cartão"),
        ("PIX", "PIX"),
        ("Deposito", "Depósito"),
        ("Outro", "Outro")
    )

    TIPSEV_CHOICES = (
        ("Banho", "Banho"),
        ("Tosa", "Tosa"),
        ("Transporte", "Transporte"),
        ("Outro", "Outro")
    )

    data = models.DateField(null=False, blank=False)
    formaPag = models.CharField(max_length=8, choices=PAG_CHOICES, blank=False, null=False)
    TipoServico = models.CharField(max_length=10, choices=TIPSEV_CHOICES, blank=False, null=False)

    cliente = models.OneToOneField(Cliente, on_delete=models.SET_NULL, null=True)
    pet = models.OneToOneField(Pet, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.TipoServico
