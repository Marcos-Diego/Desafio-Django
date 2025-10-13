from django.shortcuts import render, get_object_or_404, redirect
from.models import Receitas
from.forms import ReceitaForm
def lista_de_receitas(request):
    receitas = Receitas.objects.all()
    contexto = {'receitas': receitas}
    return render(request, 'receitas/lista_de_receitas.html', contexto)

def detalhe_da_receita(request, pk):
    receita = get_object_or_404(Receitas, pk=pk)
    contexto = {'receita': receita}
    return render(request, 'receitas/detalhe_da_receita.html', contexto)

def adicionar_receita(request):
    if request.method == 'POST':
        formulario = ReceitaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_de_receitas')
    else:
        formulario = ReceitaForm()

        contexto = {'formulario': formulario}
        return render(request, 'receitas/adicionar_receita.html', contexto)
