from django import template

register = template.Library()

@register.filter
def isfloat2nd(value):
	"""
	Checks whether the second member in a list is a float or not, return "yes" or "no". This is to specify the reccommended paper roll for a clamp-lift driver.
	"""
	finding = str(type(value[1])).find("float")
	if finding > 0: return "yes"
	else: return "no"
