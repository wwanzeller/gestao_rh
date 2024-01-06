from django.urls import path
from .views import (
    DepartamentoList,
    DepartamentoCreate,
    DepartamentoUpdate,
    DepartamentoDelete,
)


urlpatterns = [
    path('', DepartamentoList.as_view(), name='departamento-list'),
    path('criar/', DepartamentoCreate.as_view(), name='departamento-create'),
    path('atualizar/<int:pk>/', DepartamentoUpdate.as_view(), name='departamento-update'),
    path('deletar/<int:pk>/', DepartamentoDelete.as_view(), name='departamento-delete'),
]