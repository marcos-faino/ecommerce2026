from django import forms
from django.utils.translation import gettext_lazy as _

class NonceForm(forms.Form):
    payment_method_nonce = forms.CharField(
        max_length=1000,
        widget=forms.widgets.HiddenInput,
        required=False
    )

    def clean(self):
        self.cleaned_data = super().clean()
        if not self.cleaned_data.get('payment_method_nonce'):
            raise forms.ValidationError(_("Não foi possível processar o pagamento"))
        return self.cleaned_data