from django import template

register = template.Library()

@register.filter
def thirteenth(value):
	result = value[12]
	return result
