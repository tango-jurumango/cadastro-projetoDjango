from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuario
from validate_docbr import CPF
from validate_email import validate_email

def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        cpf = request.POST.get('cpf')
        email = request.POST.get("email")
        if not nome or not idade or not cpf or not email:
            messages.error(request, "Preencha todos os campos obrigatoriamente.")
        else:
            cpf_validator = CPF()
            email_validator = validate_email
            # Verificar se o CPF está formatado corretamente e se é válido
            if not cpf_validator.validate(cpf):
                messages.error(request, "Erro ao salvar o usuário, o CPF está incorreto!!!")
            elif not email_validator(email):
                messages.error(request, "Erro ao salvar o usuário, o email está incorreto!!!")
            else:
                if Usuario.objects.filter(cpf=cpf).exists():
                    messages.error(request, "Erro ao salvar o usuário, o CPF já está cadastrado!!!")
                elif Usuario.objects.filter(email=email).exists():
                    messages.error(request, "Erro ao salvar o usuário, o email já está cadastrado!!!")
                else:
                    novo_usuario = Usuario(nome=nome, idade=idade, cpf=cpf, email=email)
                    novo_usuario.save()
                    messages.success(request, "Usuário cadastrado com sucesso")
    usuarios = {'usuarios': Usuario.objects.all()}  
    return render(request, 'usuarios/usuarios.html', usuarios)

'''# Create your views here.
def home(request):
    return render(request,'usuarios/home.html')
def usuarios(request):
    #Salvar os dados da tela para o banco de dados
    novo_usuario = Usuario()
    #para pegar as informações
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    #para salvar de fato é necessário usar o save
    novo_usuario.save()
    #Exibir todos os usuarios ja cadastrados em uma nova pagina
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    #Retornar os dados para a pagina de listagem de usuários
    return render(request, 'usuarios/usuarios.html', usuarios)'''
