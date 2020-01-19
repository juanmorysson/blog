from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Noticia, Area
from .forms import NoticiaForm, AreaForm
from django.shortcuts import redirect

# Create your views here.

def inicio(request):
    noticias = Noticia.objects.all()
    return render(request, 'portal/inicio.html', {'noticias': noticias})


#Views da Area

def area_list(request):
    areas = Area.objects.all()
    return render(request, 'portal/area_list.html', {'areas': areas})

def area_detail(request, pk):
    area = get_object_or_404(Area, pk=pk)
    return render(request, 'portal/area_detail.html', {'area': area})
    
def area_new(request):
    if request.method == "POST":
        form = AreaForm(request.POST, request.FILES)
        if form.is_valid():
            area = form.save(commit=False)
            area.save()
            return redirect('area_detail', pk=area.pk)
    else:
        form = AreaForm()
    return render(request, 'portal/area_edit.html', {'form': form})
    
def area_edit(request, pk):
    area = get_object_or_404(Area, pk=pk)
    if request.method == "POST":
        form = AreaForm(request.POST, request.FILES, instance=area)
        if form.is_valid():
            area = form.save(commit=False)
            area.save()
            return redirect('area_detail', pk=area.pk)
    else:
        form = AreaForm(instance=area)
    return render(request, 'portal/area_edit.html', {'form': form})
    
def area_remove(request, pk):
    area = get_object_or_404(Area, pk=pk)
    area.delete()
    return redirect('area_list')    
    

#Views da Noticia

def noticia_list(request):
    noticias = Noticia.objects.all()
    return render(request, 'portal/noticia_list.html', {'noticias': noticias})

def noticia_detail(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    return render(request, 'portal/noticia_detail.html', {'noticia': noticia})
    
def noticia_new(request):
    if request.method == "POST":
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            noticia = form.save(commit=False)
            noticia.autor = request.user
            noticia.data_publicacao = timezone.now()
            noticia.save()
            return redirect('noticia_detail', pk=noticia.pk)
    else:
        form = NoticiaForm()
    return render(request, 'portal/noticia_edit.html', {'form': form})
    
def noticia_edit(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    if request.method == "POST":
        form = NoticiaForm(request.POST, request.FILES, instance=noticia)
        if form.is_valid():
            noticia = form.save(commit=False)
            noticia.autor = request.user
            noticia.data_publicacao = timezone.now()
            noticia.save()
            return redirect('noticia_detail', pk=noticia.pk)
    else:
        form = NoticiaForm(instance=noticia)
    return render(request, 'portal/noticia_edit.html', {'form': form})
    
def noticia_remove(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    noticia.delete()
    return redirect('noticia_list')    
    
