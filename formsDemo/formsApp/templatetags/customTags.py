from django import template
register = template.Library()

@register.filter(name='xab')
def customXablau(value):
    return value[:2].lower()
        
        
@register.filter(name='xab2')
def customXablau2(value,arg):
    return value[:arg].lower()