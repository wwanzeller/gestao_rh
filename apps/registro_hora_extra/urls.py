# from django.http import HttpResponse
from django.urls import path
from .views import (
    HoraExtraList,
)


urlpatterns = [
    # path('', lambda request: HttpResponse("Olá desde horas extras")),
    path('', HoraExtraList.as_view(), name='horaextra_list'),
]
