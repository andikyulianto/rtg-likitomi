from django import template

register = template.Library()

@register.filter
def second(value):
	result = int(value[1])
	return result
