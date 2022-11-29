from django.urls import path
from Ausentismos import views


urlpatterns = [
    path('crear/',views.crearAusentismo),
    path('listar/',views.listarAusentismo,name="listarInca"),
    path('editar/',views.editarAusentismo)
]
