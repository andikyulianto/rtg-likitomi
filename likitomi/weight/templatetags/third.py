from django import template

register = template.Library()

@register.filter
def third(value):
	result = int(value[2])
	return result
