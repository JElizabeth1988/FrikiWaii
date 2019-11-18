from django.shortcuts import render, redirect
from .models import Producto, Categoria
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, 'core/home.html')

# ---------------------------------------------------------------
def registro(request):
    lista = Categoria.objects.all()
    data = {
        'categorias' : lista
    }

    if request.POST:
        producto =  Producto()
        producto.codigo = request.POST.get("txtCodigo")
        producto.nombre = request.POST.get("txtNombre")
        producto.descripcion = request.POST.get("txtDescripcion")
        producto.precio = request.POST.get("txtPrecio")
        producto.imagen = request.FILES.get("txtImagen")

        categoria = Categoria()
        categoria.id = request.POST.get("cboCategoria")
        producto.categoria  = categoria

        try:
            producto.save()
            mensaje = "Agregado"
            messages.success(request, mensaje)
        except:
            mensaje  = "Error al agregar"
            messages.error(request, mensaje)

        return redirect('registro')

    return render(request, 'core/registro.html', data)

# ----------------------------------------------------------------------

def listado(request):
    lista = Producto.objects.all()

    data = {
        'productos' : lista
    }

    return render(request, 'core/listado.html', data)

# -----------------------------------------------------------------


def eliminar(request, id):
    auto  = Producto.objects.get(id=id)
    
    try:
        producto.delete()
        mensaje = "Eliminado"
        messages.success(request, mensaje)
    except :
        mensaje = "No se pudo eliminar" 
        messages.error(request, mensaje)

    return redirect('listado')


# ----------------------------------------------------------

def modificar(request, id):
   # variables que enviaremos a la vista
    producto = Producto.objects.get(id=id)
    categorias = Categoria.objects.all()
    variables = {
        'producto'   : producto,
        'categorias' : categorias
    }

    if request.POST:
        producto = Producto()
        # se agrega el id para poder modificarlo
        producto.id = request.POST.get('txtId')
        producto.codigo = request.POST.get('txtCodigo')
        producto.nombre = request.POST.get('txtNombre')
        producto.descripcion = request.POST.get('txtDescripcion')
        producto.precio = request.POST.get('txtPrecio')
        categoria  = categoria()
        categoria.id = request.POST.get('cboCategoria')
        producto.categoria = categoria
        try:
            producto.save()
            mensaje = "Modificado correctamente"
            messages.success(request, mensaje)
        except:
            mensaje = "Error al modificar"
            messages.error(request, mensaje)

        return redirect('listado')
        
    return render(request, 'core/modificar.html', variables)

# -----------------------------------------------------------

def alien(request):
    return render(request, 'core/alien.html')

def audifonos(request):
    return render(request, 'core/audifonos.html')

def bunny(request):
    return render(request, 'core/bunny.html')

def car_avengers(request):
    return render(request, 'core/car-avengers.html')

def car_naruto(request):
    return render(request, 'core/car-naruto.html')

def carro(request):
    return render(request, 'core/carro.html')

def crybaby(request):
    return render(request, 'core/crybaby.html')

def desc_accesorios(request):
    return render(request, 'core/desc-accesorios.html')

def desc_bags(request):
    return render(request, 'core/desc-bags.html')

def desc_gamerstyle(request):
    return render(request, 'core/desc-gamerstyle.html')

def desc_outfits(request):
    return render(request, 'core/desc-outfits.html')

def desc_papeleria(request):
    return render(request, 'core/desc-papeleria.html')

def desc_phonecase(request):
    return render(request, 'core/desc-phonecase.html')

def inosuke(request):
    return render(request, 'core/inosuke.html')

def joker(request):
    return render(request, 'core/joker.html')

def llavero(request):
    return render(request, 'core/llavero.html')

def memo(request):
    return render(request, 'core/memo.html')

def momo(request):
    return render(request, 'core/momo.html')

def muerto(request):
    return render(request, 'core/muerto.html')

def penny(request):
    return render(request, 'core/penny.html')

def pokemochila(request):
    return render(request, 'core/pokemochila.html')

def sacapuntas(request):
    return render(request, 'core/sacapuntas.html')

def sudadera(request):
    return render(request, 'core/sudadera-av.html')

    
