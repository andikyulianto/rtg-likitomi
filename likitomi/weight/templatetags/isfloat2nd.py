from django import template

register = template.Library()

@register.filter
def isfloat2nd(value):
	finding = str(type(value[1])).find("float")
	if finding > 0: return "yes"
	else: return "no"
