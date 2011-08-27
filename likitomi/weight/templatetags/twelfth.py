from django import template

register = template.Library()

@register.filter
def twelfth(value):
	"""
	Returns the number of paper rolls of weight range 400-699 kgs. for a particular location querying from the current paper roll on clamp-lift vehicle.
	"""
	result = value[11]
	return result
