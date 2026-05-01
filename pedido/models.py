from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from catalogo.models import Produto


class Pedido(models.Model):
    user = get_user_model()
    cliente = models.ForeignKey(user, on_delete=models.CASCADE)
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)
    pago = models.BooleanField(default=False)
    # mudei aqui para tentar efetuar pagamento
    braintree_id = models.CharField(max_length=150, blank=True)

    class Meta:
        ordering = ("-criado",)

    def __str__(self):
        return _('Pedido {self.id}').format(self.pk)

    def get_total_geral(self):
        return sum(item.get_total() for item in self.itens_pedido.all())


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE,
                               related_name='itens_pedido')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE,
                                related_name='itens_produto')
    preco_unit = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ('pedido',)
        verbose_name = 'Item Pedido'
        verbose_name_plural = 'Itens Pedido'

    def __str__(self):
        return _('Item {self.id} do Pedido {self.pedido.id}').format(self.pk, self.pedido.pk)

    def get_total(self):
        return self.preco_unit * self.quantidade