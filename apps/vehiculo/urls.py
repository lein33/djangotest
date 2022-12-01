from django.urls import path
from apps.vehiculo.views import saludoV,vehiculo_view,vehiculo_list
app_name='vehiculo'
urlpatterns = [
    path('saludov/', saludoV, name='index'),
    path('newv/', vehiculo_view, name='crear_vehiculo'),
    path('listv/', vehiculo_list, name='listar_vehiculo'),
]
