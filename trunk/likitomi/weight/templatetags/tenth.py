from django import template

register = template.Library()

@register.filter
def tenth(value):
	result = value[9]
	return result
