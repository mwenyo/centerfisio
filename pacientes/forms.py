from django import forms

from .models import Paciente


class PacienteForm(forms.ModelForm):
    """Form definition for Paciente."""

    class Meta:
        """Meta definition for Pacienteform."""

        model = Paciente
        fields = ('nome',
                  'data_nascimento',
                  'cpf',
                  'rg',
                  'telefone',
                  'endereco',
                  'cidade',
                  'estado',
                  'email',
                  'profissao',)

        widgets = {
            'nome': forms.TextInput(
                attrs={'class': 'form-control border-info'}),
            'data_nascimento': forms.DateInput(
                attrs={
                    'class': 'form-control border-info',
                    'data-inputmask': '\'mask\': \'99/99/9999\'',
                    'im-insert': 'true'}),
            'cpf': forms.TextInput(
                attrs={
                    'class': 'form-control border-info',
                    'data-inputmask': '\'mask\': \'999.999.999-99\'',
                    'im-insert': 'true'}),
            'rg': forms.TextInput(
                attrs={'class': 'form-control border-info'}),
            'telefone': forms.TextInput(
                attrs={
                    'class': 'form-control border-info',
                    'data-inputmask': '\'mask\': \'(99) 99999-9999\'',
                    'im-insert': 'true'}),
            'endereco': forms.TextInput(
                attrs={'class': 'form-control border-info'}),
            'cidade': forms.TextInput(
                attrs={'class': 'form-control border-info'}),
            'estado': forms.TextInput(
                attrs={'class': 'form-control border-info'}),
            'email': forms.EmailInput(
                attrs={'class': 'form-control border-info'}),
            'profissao': forms.TextInput(
                attrs={'class': 'form-control border-info'}),
        }
