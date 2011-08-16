from django import template
#from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
#@stringfilter
def tofloat(value):
	result = float(value)
	return result

#register.filter('getpos', getpos)
