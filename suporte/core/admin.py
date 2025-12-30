from django.contrib import admin
from .models import Funcionario, Aparelho, RegistroManutencao

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'cargo', 'telefone')

@admin.register(Aparelho)
class AparelhoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'tipo', 'marca', 'modelo', 'numero_serie', 'cliente', 'data_cadastro')
    search_fields = ('nome', 'numero_serie', 'cliente')

@admin.register(RegistroManutencao)
class RegistroManutencaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'aparelho', 'funcionario', 'tipo_servico', 'peca_trocada', 'data_execucao')
    search_fields = ('aparelho__nome', 'descricao')
    list_filter = ('tipo_servico', 'data_execucao')
