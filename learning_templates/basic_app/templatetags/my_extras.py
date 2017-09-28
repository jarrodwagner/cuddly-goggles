from django import template

register = template.Library()


@register.filter(name = 'fut')
def fut(value,arg):
    """
    This cuts out all values of arg from value
    """

    return value.replace(arg,'')

# register.filter('fut', fut)
