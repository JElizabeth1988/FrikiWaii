from django.shortcuts import render, redirect
from .models import Producto, Categoria, Contacto, TipoContacto
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from .forms import ProductoForm, ContactoForm

#rest_framework
# from rest_framework import viewsets
# from .serializers import FrikiwaiiSerializer

#import para notificaciones push
from django.views.decorators.http import require_http_methods
# csrf_exempt: para enviar el token
from django.views.decorators.csrf import csrf_exempt

# HttpResponse: devuelvo un json | HttpResponseBadRequest: devuelvo un error en el json
from django.http import HttpResponse, HttpResponseBadRequest

from django.core import serializers
import json

# FCMDevice: modelo dentro del pqte que representa un dispositivo
from fcm_django.models import FCMDevice
#import para notificaciones push

# Create your views here.
@csrf_exempt
@require_http_methods(['POST'])
def guardar_token(request):
    # {token:132213ghgfghf13ghf}
    body = request.body.decode('utf-8')
    bodyDict = json.loads(body)

    token = bodyDict['token']

    existe = FCMDevice.objects.filter(registration_id = token, active= True)

    if len(existe) > 0:
        #dumps transforma el diccionario a un json (lo contrario de loads)
        return HttpResponseBadRequest(json.dumps({'mensaje':'el token ya existe'}))

    dispositivo = FCMDevice()
    dispositivo.registration_id = token
    dispositivo.active = True

    #Solo si el usuario esta autenticado procedemos a enlazar
    if request.user.is_authenticated: 
        dispositivo.user = request.user
    
    try:
        dispositivo.save()
        return HttpResponse(json.dumps({'mensaje':'el token guardado'}))
    except:
        return HttpResponseBadRequest(json.dumps({'mensaje':'Error al guardar el Token'}))


def home(request):
    return render(request, 'core/home.html')

# ---------------------------------------------------------------
#restringimos permisos
@permission_required('core.add_producto')
def registro(request):
    data = {
        'form':ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
             # ---------------------------Notificaciones
            #1° Obtenemos todos los dispositivos
            # dispositivo = FCMDevice.objects.filter(active=True)
            # dispositivo.send_message(
            #     title= "Producto Agregado!",
            #     body="Se ha Agregado: " + producto.cleaned_data['nombre'],
            #     icon="static/core/img/doni.png"          
            # )
            # -------------------------------------------
            data['mensaje'] = "Guardado Correctamente"
        data['form'] = formulario
    
    return render(request, 'core/registro.html', data)

#--------------------------------------------------------------------------
def modificar(request,id):
    producto = Producto.objects.get(id=id)
    data = {
        'form': ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()

            data['mensaje']= "Modificado Correctamente"
        data['form']= ProductoForm(instance=Producto.objects.get(id=id))
            
    return render(request, 'core/modificar.html', data)




# def registro1(request):
#     lista = Categoria.objects.all()
#     data = {
#         'categorias' : lista
#     }

#     if request.POST:
#         producto =  Producto()
#         producto.codigo = request.POST.get("txtCodigo")
#         producto.nombre = request.POST.get("txtNombre")
#         producto.descripcion = request.POST.get("txtDescripcion")
#         producto.precio = request.POST.get("txtPrecio")
#         producto.imagen = request.FILES.get("txtImagen")

#         categoria = Categoria()
#         categoria.id = request.POST.get("cboCategoria")
#         producto.categoria  = categoria

#         try:
#             producto.save()

#             # ---------------------------Notificaciones
#             #1° Obtenemos todos los dispositivos
#             dispositivos = FCMDevice.objects.filter(active=True)
#             dispositivos.send_message(
#                 title= "Producto Agregado!",
#                 body="Se ha Agregado: " + producto.cleaned_data['nombre'],
#                 icon="static/core/img/doni.png"          
#             )
#             # -------------------------------------------

#             mensaje = "Agregado"
#             messages.success(request, mensaje)
#         except:
#             mensaje  = "Error al agregar"
#             messages.error(request, mensaje)

#         return redirect('registro')

#     return render(request, 'core/registro.html', data)

# ----------------------------------------------------------------------
#restringimos el método que solo funcione si estoy autenticado (requiere login)
@login_required
def listado(request):
    lista = Producto.objects.all()

    data = {
        'productos' : lista
    }

    return render(request, 'core/listado.html', data)

#Registrar CONTACTO-------------------------------------------------------
def nuevo_contacto(request):
        data = {
             'form':ContactoForm()
        }

        if request.method == 'POST':
           formulario = ContactoForm(request.POST)
           if formulario.is_valid():
               formulario.save()
               data['mensaje'] = "Guardado Correctamente"
    
        return render(request, 'core/nuevo_contacto.html', data)

#Listar CONTACTO--------------------------------------------------------- 
def listado_contacto(request):
    contactos = Contacto.objects.all()
    data = {
        'contactos':contactos
    }
    return render(request, 'core/listado_contacto.html', data)


# ----------------LISTA DE LOS PRODUCTOS CON REDIRECCION A LA PÁGINA.html--------------
def listadoOutfits(request):
    lista = Producto.objects.all()

    data = {
        'productos' : lista
    }

    return render(request, 'core/desc-outfits.html', data)

def listadoBags(request):
    lista = Producto.objects.all()

    data = {
        'productos' : lista
    }

    return render(request, 'core/desc-bags.html', data)

def listadoPapeliria(request):
    lista = Producto.objects.all()

    data = {
        'productos' : lista
    }

    return render(request, 'core/desc-papeleria.html', data)
    
def listadoAccesorios(request):
    lista = Producto.objects.all()

    data = {
        'productos' : lista
    }

    return render(request, 'core/desc-accesorios.html', data)

def listadoPhoneCase(request):
    lista = Producto.objects.all()

    data = {
        'productos' : lista
    }

    return render(request, 'core/desc-phonecase.html', data)

def listadoGamerStyle(request):
    lista = Producto.objects.all()

    data = {
        'productos' : lista
    }

    return render(request, 'core/desc-gamerstyle.html', data)

# -----------------------------------------------------------------


def eliminar(request, id):
    producto  = Producto.objects.get(id=id)
    
    try:
        producto.delete()
        mensaje = "Eliminado"
        messages.success(request, mensaje)
    except :
        mensaje = "Error al eliminar" 
        messages.error(request, mensaje)

    return redirect('listado')



# ----------------------------------------------------------

# def modificar(request, id):
#    # variables que enviaremos a la vista
#     producto = Producto.objects.get(id=id)
#     categorias = Categoria.objects.all()
#     variables = {
#         'producto'   : producto,
#         'categorias' : categorias
#     }

#     if request.POST:
#         producto = Producto()
#         # se agrega el id para poder modificarlo
#         producto.id = request.POST.get('txtId')
#         producto.codigo = request.POST.get('txtCodigo')
#         producto.nombre = request.POST.get('txtNombre')
#         producto.descripcion = request.POST.get('txtDescripcion')
#         producto.precio = request.POST.get('txtPrecio')
#         producto.imagen = request.FILES.get("txtImagen")


#         categoria  = Categoria()
#         categoria.id = request.POST.get('cboCategoria')
#         producto.categoria = categoria
#         try:
#             producto.save()
#             mensaje = "Modificado correctamente"
#             messages.success(request, mensaje)
#         except:
#             mensaje = "Error al modificar"
#             messages.error(request, mensaje)

#         return redirect('listado')
        
#     return render(request, 'core/modificar.html', variables)

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


