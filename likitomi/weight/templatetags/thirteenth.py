from django import template

register = template.Library()

@register.filter
def thirteenth(value):
	"""
	Returns the number of paper rolls of weight range >700 kgs. for a particular location querying from the current paper roll on clamp-lift vehicle.
	"""
	result = value[12]
	return result
