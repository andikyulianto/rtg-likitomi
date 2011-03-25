from django import template

register = template.Library()

@register.filter
def sixth(value):
	result = value[5]
	return result
