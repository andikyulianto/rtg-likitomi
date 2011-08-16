from django import template

register = template.Library()

@register.filter
def fifth(value):
	result = int(value[4])
	return result
