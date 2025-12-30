
from django.db import models
from django.contrib.auth.models import User

class Funcionario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    cargo = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.usuario.get_full_name() or self.usuario.username


class Aparelho(models.Model):
    TIPO_CHOICES = [
        ('NOTEBOOK', 'Notebook'),
        ('DESKTOP', 'Desktop'),
        ('IMPRESSORA', 'Impressora'),
        ('MONITOR', 'Monitor'),
        ('OUTRO', 'Outro'),
    ]

    nome = models.CharField(max_length=150)
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    numero_serie = models.CharField(max_length=100, unique=True)
    cliente = models.CharField(max_length=150)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} ({self.tipo}) - {self.cliente}"


class RegistroManutencao(models.Model):
    TIPO_SERVICO = [
        ('MANUTENCAO', 'Manutenção'),
        ('TROCA', 'Troca de Peça'),
    ]

    aparelho = models.ForeignKey(Aparelho, on_delete=models.CASCADE, related_name='registros')
    funcionario = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True)
    tipo_servico = models.CharField(max_length=20, choices=TIPO_SERVICO)
    descricao = models.TextField()
    peca_trocada = models.CharField(max_length=150, blank=True, null=True)
    data_execucao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo_servico} - {self.aparelho.nome} por {self.funcionario}"

