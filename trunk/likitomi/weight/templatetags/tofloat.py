from django import template
#from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
#@stringfilter
def tofloat(value):
	"""
	Converts a position in position list from string to float.
	"""
	result = float(value)
	return result

#register.filter('getpos', getpos)
