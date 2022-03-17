from django.db import models

class Endereco(models.Model):
    rua = models.CharField(max_length=200, null=False, blank=False)
    numero = models.IntegerField(null=False, blank=False)
    bairro = models.CharField(max_length=50, null=False, blank=False)
    cidade = models.CharField(max_length=100, null=False, blank=False)
    pais = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.rua
      
class Cliente(models.Model):
 
    nome = models.CharField(max_length=100, null=False, blank=False)
    fone = models.CharField(max_length=14, null=False, blank=False)
    CPF = models.CharField(max_length=15, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    endereco = models.ForeignKey("Endereco", on_delete=models.CASCADE, related_name='cliente')

    def __str__(self):
        return self.nome

class Animal(models.Model):
    SEXO_CHOICES = (
        ("F", "Fêmea"),
        ("M", "Masculino"),
        ("N", "Outro")
    )

    PORTE_CHOICES = (
        ("p", "Pequeno"),
        ("M", "Medio"),
        ("G", "Grande"),
        ("N", "Outro")
    )

    TIPO_CHOICES = (
        ("Gato", "Gato"),
        ("Cachorro", "Cachorro"),
        ("Outro", "Outro")
    )

    nome = models.CharField(max_length=100, null=False, blank=False)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=False, null=False)
    raca = models.CharField(max_length=20, null=False, blank=False)
    porte = models.CharField(max_length=1, choices=PORTE_CHOICES, blank=False, null=False)
    idade = models.IntegerField(null=False, blank=False)
    tipo = models.CharField(max_length=8, choices=TIPO_CHOICES, blank=False, null=False)
    cliente = models.ForeignKey("Cliente", on_delete=models.CASCADE, related_name='animal')
    
    def __str__(self):
        return self.nome

class Servico(models.Model):
    PAG_CHOICES = (
        ("Dinheiro", "Dinheiro"),
        ("Cartao", "Cartao"),
        ("PIX", "PIX"),
        ("Deposito", "Deposito"),
        ("Outro", "Outro")
    )

    TIPSEV_CHOICES = (
        ("Banho", "Banho"),
        ("Tosa", "Tosa"),
        ("Transporte", "Transporte"),
        ("Outro", "Outro")
    )

    data = models.DateField(null=False, blank=False)
    Animal = models.ForeignKey("Animal", on_delete=models.CASCADE, related_name='Servico')
    formaPag = models.CharField(max_length=8, choices=PAG_CHOICES, blank=False, null=False)
    TipoServico = models.CharField(max_length=10, choices=TIPSEV_CHOICES, blank=False, null=False)

    def __str__(self):
        return self.TipoServico