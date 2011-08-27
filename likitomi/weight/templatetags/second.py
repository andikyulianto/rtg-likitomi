from django import template

register = template.Library()

@register.filter
def second(value):
	"""
	Returns the number of paper rolls of weight range 0-99 kgs. for a particular location querying from clamp-lift plan.
	"""
	result = int(value[1])
	return result
