from django.http import HttpResponse
from django.urls import path
from .views import DocumentoCreate
urlpatterns = [
    path('', lambda request: HttpResponse('Olá, mundo!')),
    path('criar/<int:funcionario_id>/', DocumentoCreate.as_view(), name='documento_create')
]