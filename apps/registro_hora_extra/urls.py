# from django.http import HttpResponse
from django.urls import path
from .views import (
    HoraExtraCreate,
    HoraExtraList,
    HoraExtraUpdate,
    HoraExtraDelete,
)


urlpatterns = [
    # path('', lambda request: HttpResponse("Olá desde horas extras")),
    path('criar/', HoraExtraCreate.as_view(), name='horaextra_create'),
    path('atualizar/<int:pk>/', HoraExtraUpdate.as_view(), name='horaextra_update'),
    path('', HoraExtraList.as_view(), name='horaextra_list'),
    path('deletar/<int:pk>', HoraExtraDelete.as_view(), name='horaextra_delete')
]
