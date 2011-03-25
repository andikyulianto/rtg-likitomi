from django import template

import math

register = template.Library()

@register.filter
def floor(value):
	result = int(math.floor(value))
	return result
