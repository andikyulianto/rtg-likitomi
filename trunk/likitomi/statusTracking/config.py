### pc ###
item_num= 3
####################################################
## return static setting for showing items for PC ##
####################################################
def getPCItemNum():
	return item_num
	
## cv ##
speed_3cs = 120
speed_2cl = 80
speed_3clh = 20

################################
## return static running time ##
################################
def getCVSpeed(machine):
	if machine =="3CS":
		return speed_3cs
	elif machine == "2CL":
		return speed_2cl
	elif machine == "3CL-H":
		return speed_3clh
	else:
		return 0

