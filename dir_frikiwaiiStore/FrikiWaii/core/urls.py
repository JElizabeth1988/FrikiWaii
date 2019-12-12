from django.urls import path, include
from .views import home, registro,modificar,eliminar,listado,nuevo_contacto,listado_contacto, alien, audifonos,listadoGamerStyle,listadoPhoneCase,listadoAccesorios,listadoPapeliria,listadoOutfits,listadoBags, bunny, car_avengers, car_naruto, carro, crybaby, desc_accesorios, desc_bags, desc_gamerstyle, desc_outfits,desc_papeleria, desc_phonecase, inosuke, joker, llavero, memo, momo, muerto,penny, pokemochila, sacapuntas, sudadera, guardar_token, CategoriaViewset, ProductoViewset
from django.conf import settings
from django.conf.urls.static import static

#----------------------------------API---------------------------------
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Categoria', CategoriaViewset)
router.register('Producto', ProductoViewset)

#-----------------------------------------------------------------------

urlpatterns = [
    path('', home, name="home"),
    path('registro/', registro, name="registro"),
    path('modificar/<id>/', modificar, name="modificar"),
    path('listado/', listado, name="listado"),
    path('eliminar/<id>/', eliminar, name="eliminar"),
    path('nuevo_contacto/', nuevo_contacto, name="nuevo_contacto"),
    path('listado_contacto/', listado_contacto, name="listado_contacto"),
    path('SailorMoon/', alien, name="alien"),
    path('Audifonos/', audifonos, name="audifonos"),
    path('Avengers/', bunny, name="bunny"),
    path('Carcasa-avengers/', car_avengers, name="car_avengers"),
    path('Carcasa-naruto/', car_naruto, name="car_naruto"),
    path('Carro/', carro, name="carro"),
    path('unicornioKawaii/', crybaby, name="crybaby"),
    path('Accesorios/', listadoAccesorios, name="desc_accesorios"),
    path('Bags/', listadoBags, name="desc_bags"),
    path('GamerStyle/', listadoGamerStyle, name="desc_gamerstyle"),
    path('Outfits/', listadoOutfits, name="desc_outfits"),
    path('Papeleria/', listadoPapeliria, name="desc_papeleria"),
    path('PhoneCase/', listadoPhoneCase, name="desc_phonecase"),
    path('Dc/', inosuke, name="inosuke"),
    path('Extraño-Mundo-de-Jack/', joker, name="joker"),
    path('llavero/', llavero, name="llavero"),
    path('memo-Gato/', memo, name="memo"),
    path('Pusheen/', momo, name="momo"),
    path('Totoro/', muerto, name="muerto"),
    path('Pokemon/', penny, name="penny"),
    path('pokemochila/', pokemochila, name="pokemochila"),
    path('sacapuntas/', sacapuntas, name="sacapuntas"),
    path('sudadera-avengers/', sudadera, name="sudadera"), 
    path('guardar-token/',guardar_token, name='guardar_token'),

 #----------------------------------API---------------------------------
    path('api/', include(router.urls)),
#----------------------------------------------------------------------- 

]

# carga de archivos
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)