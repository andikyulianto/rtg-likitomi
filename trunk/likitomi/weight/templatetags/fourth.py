from django import template

register = template.Library()

@register.filter
def fourth(value):
	"""
	Returns the number of paper rolls of weight range 400-699 kgs. for a particular location querying from clamp-lift plan.
	"""
	result = int(value[3])
	return result
