from django import template

register = template.Library()

@register.filter
def tenth(value):
	"""
	Returns the number of paper rolls of weight range 0-99 kgs. for a particular location querying from the current paper roll on clamp-lift vehicle.
	"""
	result = value[9]
	return result
