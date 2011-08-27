from django import template

register = template.Library()

@register.filter
def sixth(value):
	"""
	Returns the number of paper rolls of weight range 0-99 kgs. for a particular location querying from search by paper code and paper size.
	"""
	result = value[5]
	return result
