from django import forms

from .models import Pedido

class PedidoModelForm(forms.ModelForm):

    class Meta:
        model = Pedido
        # mudei aqui para tentar efetuar pagamento
        exclude = ['cliente', 'pago', 'braintree_id']
