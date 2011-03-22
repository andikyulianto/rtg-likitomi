from django import template

register = template.Library()

@register.filter
def eighth(value):
	result = value[7]
	return result
