from django.urls import path
from .views import home, registro,modificar,listado, alien, audifonos, bunny, car_avengers, car_naruto, carro, crybaby, desc_accesorios, desc_bags, desc_gamerstyle, desc_outfits,desc_papeleria, desc_phonecase, inosuke, joker, llavero, memo, momo, muerto,penny, pokemochila, sacapuntas, sudadera

urlpatterns = [
    path('', home, name="home"),
    path('registro/', registro, name="registro"),
     path('modificar/', modificar, name="modificar"),
    path('listado/', listado, name="listado"),
    path('SailorMoon/', alien, name="alien"),
    path('Audifonos/', audifonos, name="audifonos"),
    path('Avengers/', bunny, name="bunny"),
    path('Carcasa-avengers/', car_avengers, name="car_avengers"),
    path('Carcasa-naruto/', car_naruto, name="car_naruto"),
    path('Carro/', carro, name="carro"),
    path('unicornioKawaii/', crybaby, name="crybaby"),
    path('Accesorios/', desc_accesorios, name="desc_accesorios"),
    path('Bags/', desc_bags, name="desc_bags"),
    path('GamerStyle/', desc_gamerstyle, name="desc_gamerstyle"),
    path('Outfits/', desc_outfits, name="desc_outfits"),
    path('Papeleria/', desc_papeleria, name="desc_papeleria"),
    path('PhoneCase/', desc_phonecase, name="desc_phonecase"),
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
    
]
