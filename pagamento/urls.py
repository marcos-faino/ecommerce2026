from django.urls import path
from . import views

urlpatterns = [
    path('pedido/<int:idpedido>/',
         views.ProcessarPgtoFormView.as_view(), name='processar_pgto'),
    path('realizado/', views.PgtoRealizadoView.as_view(),
         name='pgtorealizado'),
    path('cancelado/', views.PgtoCanceladoView.as_view(),
         name='pgtocancelado'),
]