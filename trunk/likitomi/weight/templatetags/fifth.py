from django import template

register = template.Library()

@register.filter
def fifth(value):
	"""
	Returns the number of paper rolls of weight range >700 kgs. for a particular location querying from clamp-lift plan.
	"""
	result = int(value[4])
	return result
