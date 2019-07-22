"""Forms - Pacientes"""
from django import forms
from .models import Paciente, Contato

class PacienteForm(forms.ModelForm):
    """Form definition for Paciente."""

    class Meta:
        """Meta definition for Pacienteform."""

        model = Paciente
        fields = ('nome', 'sobrenome', 'cpf', 'nascimento',
                  'telefone1', 'telefone2', 'genero', 'estado_civil', 'profissao',
                  'endereco', 'complemento', 'numero', 'bairro', 'cidade', 'uf',
                  'diabetes', 'hipertensao', 'observacoes', 'email', 'altura', 'peso')
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control input'}),
            'sobrenome': forms.TextInput(attrs={'class': 'form-control input'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control input'}),
            'nascimento': forms.DateInput(attrs={'class': 'form-control input'}),
            'telefone1': forms.TextInput(attrs={'class': 'form-control input'}),
            'telefone2': forms.TextInput(attrs={'class': 'form-control input'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
            'estado_civil': forms.Select(attrs={'class': 'form-control'}),
            'profissao': forms.TextInput(attrs={'class': 'form-control input'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control input'}),
            'complemento': forms.TextInput(attrs={'class': 'form-control input'}),
            'numero': forms.NumberInput(attrs={'class': 'form-control input'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control input'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control input'}),
            'uf': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control input'}),
            'altura': forms.NumberInput(attrs={'class': 'form-control input'}),
            'peso': forms.NumberInput(attrs={'class': 'form-control input'}),
            'diabetes': forms.CheckboxInput(attrs={'class': 'checkbox style-0'}),
            'hipertensao': forms.CheckboxInput(attrs={'class': 'checkbox style-0'}),
        }

class ContatoForm(forms.ModelForm):
    """Form definition for Contato."""

    class Meta:
        """Meta definition for Contatoform."""

        model = Contato
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(
                attrs={'class': 'form-control input'}
                ),
            'telefone1': forms.TextInput(
                attrs={'class': 'form-control input'}
                ),
            'telefone2': forms.TextInput(
                attrs={'class': 'form-control input'}
                ),
            'email': forms.EmailInput(
                attrs={'class': 'form-control input'}
                ),
        }

ContatoFormSet = forms.inlineformset_factory(
    Paciente,
    Contato,
    form=ContatoForm,
    can_delete=True,
    extra=3,
    max_num=3
)
