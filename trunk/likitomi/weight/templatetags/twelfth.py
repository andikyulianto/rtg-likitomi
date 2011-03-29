from django import template

register = template.Library()

@register.filter
def twelfth(value):
	result = value[11]
	return result
