from django.shortcuts import redirect, render, get_object_or_404
from .forms import Producto_Form
from django.contrib import messages
from .models import*
from django.db.models import Q
# Create your views here.

def main(request):
     queryset = request.GET.get("buscar")
  
     if queryset:
          posts = Post.objects.filter(
               Q(titulo_icontains = queryset)  |
               Q(descripcion = queryset) 
          ).distinct()

     return render(request,'farma/main.html')


def nuevo_producto(request):
     data = {
          'form':Producto_Form()
     }
     if request.method == 'POST':
          form = Producto_Form(request.POST, request.FILES)
          if form.is_valid():
               form.save()
               
               
          else:
               data["from"] = form     
               
     return render(request,'farma/nuevo_producto.html',data)


def lista_produtos(request):

    producto = Productos.objects.all()
    categorias = Categoria.objects.all()
      
          
    data = {'producto' : producto,'categorias' :categorias}
    return render(request,'farma/lista_productos.html', data)


def editar_produtos(request, id ):
     productos = get_object_or_404(Productos, id=id)
     categorias = Categoria.objects.all()

     data = {
          'form':Producto_Form(instance=productos), 'categorias': categorias
     }
     if request.method == 'POST':
          form = Producto_Form(data=request.POST, instance=productos, files=request.FILES)
          if form.is_valid():
               form.save()
               return redirect  ("lista" )
               
          data ['form'] = 'form'

     return render(request, 'farma/modificar.html',data) 



def elimanar_producto(request, id):
     productos = get_object_or_404(Productos, id=id)
     productos.delete()
     messages.success(request, 'Producto Eliminado ')
     return redirect  ("lista" )
