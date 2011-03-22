from django import template

register = template.Library()

@register.filter
def ninth(value):
	result = value[8]
	return result
