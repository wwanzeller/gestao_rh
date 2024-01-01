from django.urls import path
from .views import DepartamentoList


urlpatterns = [
    path('', DepartamentoList.as_view(), name='departamento_list'),
]