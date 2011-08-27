from django import template

register = template.Library()

@register.filter
def third(value):
	"""
	Returns the number of paper rolls of weight range 100-399 kgs. for a particular location querying from clamp-lift plan.
	"""
	result = int(value[2])
	return result
