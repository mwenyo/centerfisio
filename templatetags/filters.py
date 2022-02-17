from django import template

register = template.Library()


@register.filter
def troca_virgula_ponto(value):
    if not value:
        return "0.0000"
    else:
        return str(value)
