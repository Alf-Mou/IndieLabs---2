from django.shortcuts import render, redirect

from usuarios.forms import LoginForms, CadastroForms

from django.contrib.auth.models import User

from django.contrib import auth, messages

def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome = form.cleaned_data['nome_completo']
            senha = form.cleaned_data['senha']
        print(nome, senha)
        usuario = auth.authenticate(
                request,
                username=nome,
                password=senha
            )
        print(usuario)
        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, f"Você foi logado com sucesso!")
            return redirect('index')
        else:
            messages.error(request, f"Erro ao efetuar login")
            return redirect('login')

    return render(request, 'usuarios/login.html', {"form": form})

def cadastro(request):
    form = CadastroForms()
    
    if request.method == 'POST':
        form = CadastroForms(request.POST)
        
        if form.is_valid():

            nome=form["nome_completo"].value()
            email=form["email"].value()
            senha=form["senha"].value()
            

            if User.objects.filter(username=nome).exists():
                return redirect('cadastro')
            
            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha,
            )

            usuario.save()
            return redirect('login')
        

    return render(request, 'usuarios/cadastro.html', {"form": form})


