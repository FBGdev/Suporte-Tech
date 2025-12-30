from django.shortcuts import render, redirect
from .models import Aparelho, RegistroManutencao, Funcionario
from .forms import AparelhoForm, ManutencaoForm
from django.contrib.auth.decorators import login_required
from .forms import CadastroUsuarioForm
from django.contrib.auth import login
from django.shortcuts import get_object_or_404



def home(request):
    aparelhos = Aparelho.objects.all().order_by('-data_cadastro')
    return render(request, 'home.html', {'aparelhos': aparelhos})

def cadastrar_aparelho(request):
    if request.method == 'POST':
        form = AparelhoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AparelhoForm()
    return render(request, 'cadastrar_aparelho.html', {'form': form})

def registrar_manutencao(request, aparelho_id):
    aparelho = get_object_or_404(Aparelho, id=aparelho_id)

    
    funcionario, criado = Funcionario.objects.get_or_create(
        usuario=request.user,
        defaults={"cargo": "Técnico", "telefone": ""}
    )

    if request.method == 'POST':
        form = ManutencaoForm(request.POST)
        if form.is_valid():
            registro = form.save(commit=False)
            registro.aparelho = aparelho
            registro.funcionario = funcionario
            registro.save()
            return redirect('home')
    else:
        form = ManutencaoForm()

    return render(request, 'registrar_manutencao.html', {
        'form': form,
        'aparelho': aparelho,
        'funcionario': funcionario
    })


@login_required
def home(request):
    aparelhos = Aparelho.objects.all().order_by('-data_cadastro')
    return render(request, 'home.html', {'aparelhos': aparelhos})


def cadastrar_usuario(request):
    if request.method == "POST":
        form = CadastroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['senha'])
            user.save()

            # cria o perfil de funcionário
            Funcionario.objects.create(
                usuario=user,
                cargo=form.cleaned_data['cargo'],
                telefone=form.cleaned_data['telefone']
            )

            login(request, user)
            return redirect('home')
    else:
        form = CadastroUsuarioForm()

    return render(request, 'cadastro.html', {'form': form})
