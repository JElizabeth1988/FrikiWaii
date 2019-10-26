from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name="home"),
    # path('registro/', registro, name="registro"),
    # path('listar/', listar_automoviles, name="listar"),
]
