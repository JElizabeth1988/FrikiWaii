from django.urls import path
from .views import home, alien, audifonos, bunny, car_avengers, car_naruto, carro, crybaby, desc_accesorios, desc_bags, desc_gamerstyle, desc_outfits,desc_papeleria, desc_phonecase, inosuke, joker, llavero, memo, momo, muerto,penny, pokemochila, sacapuntas, sudadera

urlpatterns = [
    path('', home, name="home"),
    path('Alien/', alien, name="alien"),
    path('Audifonos/', audifonos, name="audifonos"),
    path('Mascara-bunny/', bunny, name="bunny"),
    path('Carcasa-avengers/', car_avengers, name="car_avengers"),
    path('Carcasa-naruto/', car_naruto, name="car_naruto"),
    path('Carro/', carro, name="carro"),
    path('Mascara-cry-baby/', crybaby, name="crybaby"),
    path('Accesorios/', desc_accesorios, name="desc_accesorios"),
    path('Bags/', desc_bags, name="desc_bags"),
    path('GamerStyle/', desc_gamerstyle, name="desc_gamerstyle"),
    path('Outfits/', desc_outfits, name="desc_outfits"),
    path('Papeleria/', desc_papeleria, name="desc_papeleria"),
    path('PhoneCase/', desc_phonecase, name="desc_phonecase"),
    path('Inosuke/', inosuke, name="inosuke"),
    path('Mascara-Joker/', joker, name="joker"),
    path('llavero/', llavero, name="llavero"),
    path('memo-Gato/', memo, name="memo"),
    path('Mascara-momo/', momo, name="momo"),
    path('mascara-muerto/', muerto, name="muerto"),
    path('mascara-pennywise/', penny, name="penny"),
    path('pokemochila/', pokemochila, name="pokemochila"),
    path('sacapuntas/', sacapuntas, name="sacapuntas"),
    path('sudadera-avengers/', sudadera, name="sudadera"), 
]
