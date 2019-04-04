"""Forms - Funcionários"""
from django import forms
from .models import Funcionario, Instrutor


class FuncionarioCreateForm(forms.ModelForm):
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
        cleaned_data = super(FuncionarioCreateForm, self).clean()
        password = cleaned_data.get("senha")
        confirm_password = cleaned_data.get("confirmar_senha")

        if password != confirm_password:
            raise forms.ValidationError(
                "Senhas não conferem"
            )

class FuncionarioUpdateForm(forms.ModelForm):
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

    class Meta:
        model = Funcionario
        fields = ('nome_usuario', 'email', 'nome', 'sobrenome',
                  'cpf', 'nascimento', 'contratacao', 'telefone1',
                  'telefone2', 'endereco', 'complemento',
                  'numero', 'bairro', 'cidade', 'uf', 'estado_civil', 'genero',
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

            'endereco': forms.TextInput(attrs={'class': 'form-control input'}),

            'complemento': forms.TextInput(attrs={'class': 'form-control input'}),

            'numero': forms.NumberInput(attrs={'class': 'form-control input'}),

            'bairro': forms.TextInput(attrs={'class': 'form-control input'}),

            'cidade': forms.TextInput(attrs={'class': 'form-control input'}),

            'uf': forms.Select(attrs={'class': 'form-control'}),
        }

class FisioterapeutaCreateForm(FuncionarioCreateForm):
    """FisioterapeutaForm definition."""
    crefito = forms.CharField(max_length=150,
                              required=True,
                              widget=forms.TextInput(attrs={'class': 'form-control input'})
                             )

    especializacao = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    cursos = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

class FisioterapeutaUpdateForm(FuncionarioUpdateForm):
    """FisioterapeutaForm definition."""
    crefito = forms.CharField(max_length=150,
                              required=True,
                              widget=forms.TextInput(attrs={'class': 'form-control input'})
                             )

    especializacao = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    cursos = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

class EsteticistaCreateForm(FuncionarioCreateForm):
    """FisioterapeutaForm definition."""

    cursos = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

class EsteticistaUpdateForm(FuncionarioUpdateForm):
    """FisioterapeutaForm definition."""

    cursos = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

class InstrutorCreateForm(FuncionarioCreateForm):
    """FisioterapeutaForm definition."""
    conselho = forms.ChoiceField(required=True,
                                 choices=Instrutor.CONSELHO_CHOICE,
                                 widget=forms.Select(
                                     attrs={'class': 'form-control'})
                                )

    registro = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control input'}))

    cursos = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control'}))

class InstrutorUpdateForm(FuncionarioUpdateForm):
    """FisioterapeutaForm definition."""
    conselho = forms.ChoiceField(required=True,
                                 choices=Instrutor.CONSELHO_CHOICE,
                                 widget=forms.Select(
                                     attrs={'class': 'form-control'})
                                )

    registro = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control input'}))

    cursos = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control'}))
