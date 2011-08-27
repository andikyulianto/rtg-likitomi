from django import template

register = template.Library()

@register.filter
def seventh(value):
	"""
	Returns the number of paper rolls of weight range 100-399 kgs. for a particular location querying from search by paper code and paper size.
	"""
	result = value[6]
	return result
