from django import template

# Necessário para registrarmos um novo filtro no Django
register = template.Library()


@register.filter()
def remainder(n):
    return n % 3