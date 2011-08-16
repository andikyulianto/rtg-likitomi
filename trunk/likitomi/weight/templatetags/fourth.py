from django import template

register = template.Library()

@register.filter
def fourth(value):
	result = int(value[3])
	return result
