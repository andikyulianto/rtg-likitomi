from django import template
#from django.template.defaultfilters import stringfilter
from weight.models import PaperRoll, PaperHistory

register = template.Library()

@register.filter
#@stringfilter
def listfortag(value):
	vstr = str(value)
	split = vstr.split(".")
	result = split[1]
	return result

#register.filter('listfortag', listfortag)
