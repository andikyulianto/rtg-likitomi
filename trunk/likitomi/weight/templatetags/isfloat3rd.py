from django import template

register = template.Library()

@register.filter
def isfloat3rd(value):
	finding = str(type(value[2])).find("float")
	if finding > 0: return "yes"
	else: return "no"
