""" Formulários """

from django import forms

from .models import Procedimento
from .models import Promocao
from .models import ProcedimentoPromocao


class ProcedimentoForm(forms.ModelForm):
    """Form definition for Procedimento."""

    class Meta:
        """Meta definition for Procedimentoform."""

        model = Procedimento
        fields = ['nome', 'descricao', 'duracao', 'valor']


class PromocaoForm(forms.ModelForm):
    """Form definition for Procedimento."""

    class Meta:
        """Meta definition for Procedimentoform."""

        model = Promocao
        fields = ['descricao', 'inicio', 'termino']


class ProcedimentoPromocaoForm(forms.ModelForm):
    """Form definition for ProcedimentoPromocao."""

    class Meta:
        """Meta definition for Procedimentoform."""

        model = ProcedimentoPromocao
        fields = ['procedimento', 'promocao', 'valor_promocional']
