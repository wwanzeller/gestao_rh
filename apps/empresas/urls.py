from django.urls import path

from .views import EmpresaCreate, EmpresaUpdate


urlpatterns = [
    path('novo', EmpresaCreate.as_view(), name='empresa_create'),
    path('atualizar/<int:pk>/', EmpresaUpdate.as_view(), name='empresa_update'),
]
