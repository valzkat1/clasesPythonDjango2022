from django.urls import path
from Usuarios import views

urlpatterns = [ 
                path('crear/',views.crearUsuarios),               

]