from django import forms
from django.forms import TextInput, Select, Textarea
from .models import Aparelho, RegistroManutencao
from django.contrib.auth.models import User


class AparelhoForm(forms.ModelForm):
    class Meta:
        model = Aparelho
        fields = '__all__'
        widgets = {
            'nome': TextInput(attrs={'class': 'form-control'}),
            'tipo': Select(attrs={'class': 'form-select'}),
            'marca': TextInput(attrs={'class': 'form-control'}),
            'modelo': TextInput(attrs={'class': 'form-control'}),
            'numero_serie': TextInput(attrs={'class': 'form-control'}),
            'cliente': TextInput(attrs={'class': 'form-control'}),
        }

class ManutencaoForm(forms.ModelForm):
    class Meta:
        model = RegistroManutencao
        fields = ['tipo_servico', 'descricao', 'peca_trocada']
        widgets = {
            'tipo_servico': Select(attrs={'class': 'form-select'}),
            'descricao': Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'peca_trocada': TextInput(attrs={'class': 'form-control'}),
        }


class CadastroUsuarioForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label="Senha")
    confirmar_senha = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label="Confirmar senha")
    cargo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Cargo")
    telefone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Telefone", required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': TextInput(attrs={'class': 'form-control'}),
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
            'email': TextInput(attrs={'class': 'form-control'}),
            'email': TextInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned = super().clean()
        if cleaned.get("senha") != cleaned.get("confirmar_senha"):
            raise forms.ValidationError("As senhas não coincidem!")
        return cleaned
