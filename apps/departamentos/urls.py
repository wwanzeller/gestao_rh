from django.urls import path
from .views import (
    DepartamentoList,
    DepartamentoCreate,
    DepartamentoUpdate,
    DepartamentoDelete,
)


urlpatterns = [
    path('', DepartamentoList.as_view(), name='departamento_list'),
    path('criar/', DepartamentoCreate.as_view(), name='departamento_create'),
    path('atualizar/<int:pk>/', DepartamentoUpdate.as_view(), name='departamento_update'),
    path('deletar/<int:pk>/', DepartamentoDelete.as_view(), name='departamento_delete'),
]