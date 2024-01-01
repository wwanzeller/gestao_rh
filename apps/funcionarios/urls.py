from django.urls import path
from .views import (
    FuncionarioList,
    FuncionarioUpdate,
    FuncionarioDelete,
    FuncionarioCreate
)


urlpatterns = [
    path('', FuncionarioList.as_view(), name='funcionario_list'),
    path('atualizar/<int:pk>/', FuncionarioUpdate.as_view(), name='funcionario_update'),
    path('deletar/<int:pk>/', FuncionarioDelete.as_view(), name='funcionario_delete'),
    path('criar/', FuncionarioCreate.as_view(), name='funcionario_create'),
]
