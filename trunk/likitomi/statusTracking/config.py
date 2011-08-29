### pc ###
item_num= 3
path ="/django/likitomi"

pathERP = "http://localhost/ERP/likitomi/"
####################################################
## return static setting for showing items for PC ##
####################################################
def getPCItemNum():
	return item_num
	
## cv ##
speed_3cs = 120
speed_2cl = 80

################################
## return static running time ##
################################
def getCVSpeed(machine):
	if machine =="3CS":
		return speed_3cs
	elif machine == "2CL":
		return speed_2cl
	else:
		return 0


def rootPath():
	return path
def ERPPath():
	return pathERP
