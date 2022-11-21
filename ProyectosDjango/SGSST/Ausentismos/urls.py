from django.urls import path
from Ausentismos import views


urlpatterns = [
    path('crear/',views.crearAusentismo),
]
