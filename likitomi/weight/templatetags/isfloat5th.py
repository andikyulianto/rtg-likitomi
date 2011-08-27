from django import template

register = template.Library()

@register.filter
def isfloat5th(value):
	"""
	Checks whether the fifth member in a list is a float or not, return "yes" or "no". This is to specify the reccommended paper roll for a clamp-lift driver.
	"""
	finding = str(type(value[4])).find("float")
	if finding > 0: return "yes"
	else: return "no"
