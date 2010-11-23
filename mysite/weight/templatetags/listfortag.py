from django import template
#from django.template.defaultfilters import stringfilter
from weight.models import PaperRoll, PaperHistory

register = template.Library()

@register.filter
#@stringfilter
def listfortag(value, arg):
	
	return arg

#register.filter('listfortag', listfortag)
