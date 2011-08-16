from django import template

register = template.Library()

@register.filter
def isfloat5th(value):
	finding = str(type(value[4])).find("float")
	if finding > 0: return "yes"
	else: return "no"
