from django import template

register = template.Library()

@register.filter
def eighth(value):
	"""
	Returns the number of paper rolls of weight range 400-699 kgs. for a particular location querying from search by paper code and paper size.
	"""
	result = value[7]
	return result
