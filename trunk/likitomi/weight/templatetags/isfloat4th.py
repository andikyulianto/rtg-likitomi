from django import template

register = template.Library()

@register.filter
def isfloat4th(value):
	finding = str(type(value[3])).find("float")
	if finding > 0: return "yes"
	else: return "no"
