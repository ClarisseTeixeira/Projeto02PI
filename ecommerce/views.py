from django.shortcuts import render,get_object_or_404,redirect
from .models import Produto, Marca
from .forms import ProdutoForm, MarcaForm
from django.contrib import messages
# Create your views here.

def produto_editar(request, id):
    produto = get_object_or_404(Produto,id=id)
   
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES,instance=produto)

        if form.is_valid():            
            form.save()
            return redirect('produto_listar')

    else:
        form = ProdutoForm(instance=produto)

    return render(request,'ecommerce/form.html',{'form':form})

def produto_remover(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()
    return redirect('produto_listar') # procure um url com o nome 'lista_aluno'


def produto_criar(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto criado com sucesso!')
            form = ProdutoForm()
    else:
        form = ProdutoForm()

    return render(request, "ecommerce/form.html", {'form': form})


def produto_listar(request):
    produtos = Produto.objects.all()
    context = {
        'produtos': produtos
    }
    return render(request, "ecommerce/produtos.html", context)

def index(request):
    produtos = Produto.objects.all()
    context = {
        'produtos': produtos
    }
    return render(request, "ecommerce/index.html", context)


def home(request):
    return render(request, "ecommerce/home.html",)



def produto_detalhes(request, id): 
    produto = get_object_or_404(Produto, id=id)
    context = {
        'produto': produto
    }
    return render(request, "ecommerce/detalhes.html", context)



def marca_editar(request,id):
    marca = get_object_or_404(Marca,id=id)
   
    if request.method == 'POST':
        form = MarcaForm(request.POST, request.FILES,instance=marca)

        if form.is_valid():
            form.save()
            return redirect('marca_listar')
    else:
        form = MarcaForm(instance=marca)

    return render(request,'ecommerce/formmarcas.html',{'form':form})

def marca_remover(request, id):
    marca = get_object_or_404(Marca, id=id)
    marca.delete()
    return redirect('marca_listar') # procure um url com o nome 'lista_aluno'


def marca_criar(request):
    if request.method == 'POST':
        form = MarcaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = MarcaForm()
    else:
        form = MarcaForm()

    return render(request, "ecommerce/formmarcas.html", {'form': form})


def marca_listar(request):
    marcas = Marca.objects.all()
    context = {
        'marcas': marcas
    }
    return render(request, "ecommerce/marcas.html", context)



