from django import template

register = template.Library()

@register.filter
def eleventh(value):
	result = value[10]
	return result
