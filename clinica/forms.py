"""Forms - Clínica"""
from django import forms
from .models import Pacote

class PacoteForm(forms.ModelForm):
    """Form definition for Pacote."""

    class Meta:
        """Meta definition for Pacoteform."""

        model = Pacote
        fields = ('tipo', 'nome', 'descricao', 'valor', 'promocao', 'inicio', 'termino', 'status')
        widgets = {
            'promocao': forms.CheckboxInput(attrs={'onclick':'teste2(this)'})
        }

    def clean(self):
        cleaned_data = super(PacoteForm, self).clean()
        if not cleaned_data.get("promocao"):
            cleaned_data["inicio"] = None
            cleaned_data["termino"] = None
