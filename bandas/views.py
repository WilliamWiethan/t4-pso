from django.shortcuts import render, get_object_or_404, redirect
from .models import Banda
from .forms import BandaForm

def lista_bandas(request):
    bandas = Banda.objects.all()
    return render(request, 'lista_bandas.html', {'bandas': bandas})

def new_banda(request):
    error = False
    if request.method == 'POST':
        form = BandaForm(request.POST)
        if form.is_valid():
            form.save()
            bandas = Banda.objects.all()
            return redirect('list')
        else:
            error = True
    else:
        form = BandaForm()
        return render(request, 'new_banda.html',  { 'form': form, 'error': error })

def search_banda(request):
    search_word = request.GET.get('banda', None)
    bandas = Banda.objects.filter(nome__icontains = search_word)
    return render(request, 'lista_bandas.html', {'bandas': bandas})

def edit_banda(request, pk):
    banda = get_object_or_404(Banda, pk=pk)
    if request.method == "POST":
        form = BandaForm(request.POST, instance=banda)
        if form.is_valid():
            banda = form.save()
            return redirect('list')
    else:
        form = BandaForm(instance=banda)
    return render(request, 'edit_banda.html',
                  {'form': form, 'pk': pk})

def delete_banda(request, pk):
    banda = get_object_or_404(Banda, pk=pk)
    banda.delete()
    return redirect('list')