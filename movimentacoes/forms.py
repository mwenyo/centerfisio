""" Formulários """

from django import forms

from .models import FormaDePagamento


class FormaDePagamentoForm(forms.ModelForm):
    """Form definition for FormaDePagamento."""

    class Meta:
        """Meta definition for FormaDePagamentoform."""

        model = FormaDePagamento
        fields = ('nome', 'acrescimo', 'desconto')
