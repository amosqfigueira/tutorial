
from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index')  # quando nao e passado nenhuma pagina
]
