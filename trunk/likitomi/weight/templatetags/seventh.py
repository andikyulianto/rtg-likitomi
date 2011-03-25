from django import template

register = template.Library()

@register.filter
def seventh(value):
	result = value[6]
	return result
