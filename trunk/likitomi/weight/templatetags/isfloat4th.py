from django import template

register = template.Library()

@register.filter
def isfloat4th(value):
	"""
	Checks whether the forth member in a list is a float or not, return "yes" or "no". This is to specify the reccommended paper roll for a clamp-lift driver.
	"""
	finding = str(type(value[3])).find("float")
	if finding > 0: return "yes"
	else: return "no"
