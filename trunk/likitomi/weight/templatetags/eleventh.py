from django import template

register = template.Library()

@register.filter
def eleventh(value):
	"""
	Returns the number of paper rolls of weight range 100-399 kgs. for a particular location querying from the current paper roll on clamp-lift vehicle.
	"""
	result = value[10]
	return result
