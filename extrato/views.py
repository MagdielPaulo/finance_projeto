from django.shortcuts import render
from perfil.models import Categoria, Conta


def novo_valor(request):
    if request.method == 'GET':
        contas = Contas.objects.all()
        categorias = Categoria.objects.all()
        return render (request, 'novo_valor.html',{'contas': contas, 'categorias': categorias})
    
