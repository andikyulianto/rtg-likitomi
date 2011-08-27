from django import template

register = template.Library()

@register.filter
def ninth(value):
	"""
	Returns the number of paper rolls of weight range >700 kgs. for a particular location querying from search by paper code and paper size.
	"""
	result = value[8]
	return result
