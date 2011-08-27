from django import template
#from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
#@stringfilter
def getpos(value):
	"""
	Returns the position from the list of ('lane', 'position', 'likitomi Roll ID').
	"""
	vstr = str(value)
	split = vstr.split(".")
	result = split[1]
	return result

#register.filter('getpos', getpos)
