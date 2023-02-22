<<<<<<< HEAD
from django.shortcuts import render, redirect
from .models import Cliente, Vendedor, Compra
from .forms import ClienteFormulario, VendedorFormulario, CompraFormulario
from django.http import HttpResponse
=======
from django.shortcuts import render

>>>>>>> 0700b2c480ce15c9ab23972ea956a2196f857578
# Create your views here.


def inicio(request):
    return render(request, 'AppCoder/inicio.html')


def compra(request):
    return render(request, 'AppCoder/compra.html')

def vendedor(request):
    return render(request, 'AppCoder/vendedor.html')

def cliente(request):
    return render(request, 'AppCoder/cliente.html')

<<<<<<< HEAD

# ----------------FORMULARIOS--------------

#CLIENTE
def cliente_formulario(request):
    if request.method == 'POST':
        mi_formulario = ClienteFormulario(request.POST)
        
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            nuevo_cliente = Cliente(nombre=informacion['nombre'], apellido=informacion['apellido']) 
            
            nuevo_cliente.save()
            return redirect('inicio')
    
    mi_formulario = ClienteFormulario()
    return render(request, 'AppCoder/cliente_formulario.html', {'formulario_cliente': mi_formulario})


#VENDEDOR
def vendedor_formulario(request):
    if request.method == 'POST':
        mi_formulario = VendedorFormulario(request.POST)
        
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            nuevo_vendedor = Vendedor(nombre=informacion['nombre'], apellido=informacion['apellido'])
            
            nuevo_vendedor.save()
            return redirect('inicio')

    mi_formulario = VendedorFormulario()
    return render(request, 'AppCoder/vendedor_formulario.html', {'formulario_vendedor': mi_formulario})


#COMPRA
def compra_formulario(request):
    if request.method == 'POST':
        mi_formulario = CompraFormulario(request.POST)
        
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            nueva_compra = Compra(producto=informacion['producto'], precio=informacion['precio'], enviado=informacion['enviado'])
            
            nueva_compra.save()
            return redirect('inicio')

    mi_formulario = CompraFormulario()
    return render(request, 'AppCoder/compra_formulario.html', {'formulario_compra': mi_formulario})



#- ----------------------BUSQUEDA------------------

def busqueda_cliente(request):
    return render (request, 'AppCoder/busqueda_cliente.html')

# def buscar(request):
    
#     if request.GET['nombre']:
#         mi_nombre = request.GET['nombre']
#         resultado = Cliente.objects.filter(nombre__icontains= mi_nombre)
        
#         return render(request, 'AppCoder/resultados_busqueda.html', {'cliente':resultado, 'nombre':mi_nombre})
    
    
#     respuesta= 'No se encontro ese cliente'
     
#     return HttpResponse(respuesta)
# def buscar(request):
#     if request.GET['nombre']:
#        mi_nombre = request.GET['nombre']
#        clientes = Cliente.objects.filter(nombre__icontains=mi_nombre)

#        return render(request, 'AppCoder/busqueda_cliente.html', {'cliente': clientes, 'nombre': mi_nombre})
   

#     else:
#         respuesta = "No se encontro informacion"

#     return HttpResponse(respuesta)
def buscar(request):
    if request.GET['nombre']:
       mi_nombre = request.GET['nombre']
       resultados = Cliente.objects.filter(nombre__icontains=mi_nombre)

       return render(request, 'AppCoder/resultados_busqueda.html', {'clientes': resultados, 'nombre': mi_nombre})

    else:
        respuesta = "No se encontró información"

    return HttpResponse(respuesta)

=======
>>>>>>> 0700b2c480ce15c9ab23972ea956a2196f857578
