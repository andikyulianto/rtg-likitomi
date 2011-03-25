from django import template

register = template.Library()

@register.filter
def second(value):
	result = value[1]
	return result
