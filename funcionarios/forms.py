"""Forms - Funcionários"""
from django import forms
from .models import Funcionario, Fisioterapeuta, Esteticista, Instrutor


class FuncionarioForm(forms.ModelForm):
    """FuncionarioForm definition."""

    nome_usuario = forms.CharField(max_length=150, required=True,
                                   widget=forms.TextInput(
                                       attrs={'class': 'form-control input'}))
    email = forms.EmailField(required=True,
                             widget=forms.EmailInput(
                                 attrs={'class': 'form-control input'})
                             )
    nome = forms.CharField(max_length=30, required=True,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control input'})
                           )
    sobrenome = forms.CharField(max_length=150, required=True,
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control input'})
                                )
    senha = forms.CharField(max_length=200, required=True,
                            widget=forms.PasswordInput(
                                attrs={'class': 'form-control input'})
                            )
    confirmar_senha = forms.CharField(max_length=200, required=True,
                                      widget=forms.PasswordInput(
                                          attrs={'class': 'form-control input',})
                                      )

    class Meta:
        model = Funcionario
        fields = ('nome_usuario', 'email', 'nome', 'sobrenome', 'senha', 'confirmar_senha',
                  'cpf', 'nascimento', 'contratacao', 'telefone1',
                  'telefone2', 'endereco', 'complemento',
                  'numero', 'bairro', 'cidade', 'uf', 'estado_civil', 'genero', 'foto',
                  )
        widgets = {
            'cpf': forms.TextInput(attrs={'class': 'form-control input',
                                          'data-mask': '999.999.999-99',
                                          'data-mask-placeholder':'_'}),

            'nascimento': forms.DateInput(attrs={'class': 'form-control input',
                                                 'data-mask': '99/99/9999',
                                                 'data-mask-placeholder':'_'}),

            'contratacao': forms.DateInput(attrs={'class': 'form-control input',
                                                  'data-mask': '99/99/9999',
                                                  'data-mask-placeholder':'_'}),

            'telefone1': forms.TextInput(attrs={'class': 'form-control input',
                                                'data-mask': '(99) 9999-9999',
                                                'data-mask-placeholder':'_'}),

            'telefone2': forms.TextInput(attrs={'class': 'form-control input',
                                                'data-mask': '(99) 9999-9999',
                                                'data-mask-placeholder':'_'}),

            'estado_civil': forms.Select(attrs={'class': 'form-control'}),

            'genero': forms.Select(attrs={'class': 'form-control'}),

            'foto': forms.FileInput(attrs={'class': 'form-control input'}),

            'endereco': forms.TextInput(attrs={'class': 'form-control input'}),

            'complemento': forms.TextInput(attrs={'class': 'form-control input'}),

            'numero': forms.NumberInput(attrs={'class': 'form-control input'}),

            'bairro': forms.TextInput(attrs={'class': 'form-control input'}),

            'cidade': forms.TextInput(attrs={'class': 'form-control input'}),

            'uf': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super(FuncionarioForm, self).clean()
        password = cleaned_data.get("senha")
        confirm_password = cleaned_data.get("confirmar_senha")

        if password != confirm_password:
            raise forms.ValidationError(
                "Senhas não conferem"
            )


class FisioterapeutaForm(forms.ModelForm):
    """FisioterapeutaForm definition."""
    class Meta:
        """Meta definition for Esteticistaform."""

        model = Fisioterapeuta
        fields = ('crefito', 'especializacao', 'cursos',)


class EsteticistaForm(forms.ModelForm):
    """Form definition for Esteticista."""

    class Meta:
        """Meta definition for Esteticistaform."""

        model = Esteticista
        fields = ('cursos',)


class InstrutorForm(forms.ModelForm):
    """Form definition for Instrutor."""

    class Meta:
        """Meta definition for Instrutorform."""

        model = Instrutor
        fields = ('conselho', 'registro', 'cursos',)
