from django import template

register = template.Library()

@register.filter
def third(value):
	result = value[2]
	return result
