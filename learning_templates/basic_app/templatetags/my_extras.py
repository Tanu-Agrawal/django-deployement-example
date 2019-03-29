from django import template

# CREATE AN OBJECT 'register'
register = template.Library()

# REGISTER THIS CUSTOM FILTER 'cut'(METHOD [1]) using decorators
@register.filter(name='cut')
# FUNCTION OF CUSTOM TEMPLATE FILTER
def cut(value,arg):
    """
    This cuts out all values of args from the String!
    """
    return value.replace(arg,'')

# REGISTER THIS CUSTOM FILTER 'cut'(METHOD [2])
# register.filter('cut',cut)
