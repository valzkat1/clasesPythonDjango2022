from django.urls import path
from Usuarios import views

urlpatterns = [ 
                path('crear/',views.crearUsuarios), 
                path('listar/',views.listarUsuarios,name="listaUsu"),
                path('editar/',views.edicionUsuarios,name="editaUsu"),
                path('eliminar/',views.eliminarUsuario)              

]