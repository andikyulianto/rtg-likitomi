# Create your views here.
from django.shortcuts import render_to_response
from mysite.weight.models import PaperRoll, PaperHistory

import serial
import socket
import random

def scale(request):
# Connect serial port #
	try:
		weight = 'None'

		operating_mode = 'real' # Operating mode = {'real', 'fake'} #

		scale_mode = 'fake'

		if scale_mode == 'real':

			ser = serial.Serial()
			ser.port = '/dev/ttyUSB0'
			ser.baudrate = 2400
			ser.bytesize = 7
			ser.parity = 'E'
			ser.stopbits = 1
			ser.timeout = 2
			ser.open()
			ser.flushInput()
			output = ser.readline()
			ser.close()
			a = output.rsplit(",")
			if len(a) == 3:
				if a[0] == 'US':
					b = a[2]
					if b[0:1] == '+':
						c = b[-11:]
						d = c[:-4]
						weight = float(d)
						digital = str(weight)
						if len(digital) == 7:
							digit1 = digital[0:1]
							digit2 = digital[1:2]
							digit3 = digital[2:3]
							digit4 = digital[3:4]
							digit5 = digital[4:5]
							digit6 = digital[5:6]
							digit7 = digital[6:7]
						if len(digital) == 6:
							digit2 = digital[0:1]
							digit3 = digital[1:2]
							digit4 = digital[2:3]
							digit5 = digital[3:4]
							digit6 = digital[4:5]
							digit7 = digital[5:6]
						if len(digital) == 5:
							digit3 = digital[0:1]
							digit4 = digital[1:2]
							digit5 = digital[2:3]
							digit6 = digital[3:4]
							digit7 = digital[4:5]
						if len(digital) == 4:
							digit4 = digital[0:1]
							digit5 = digital[1:2]
							digit6 = digital[2:3]
							digit7 = digital[3:4]
						if len(digital) == 3:
							digit5 = digital[0:1]
							digit6 = digital[1:2]
							digit7 = digital[2:3]
					else:
						serror = "[The weight is negative.]"
				else:
					serror = "[The weight is overloaded.]"
			else:
				serror = "[Data sent is not complete.]"

		if scale_mode == 'fake':

			output = "US,NT,+00325.5Kg\r\n"
			weight = round(random.uniform(1,500),0)
			digital = str(weight)
			if len(digital) == 7:
				digit1 = digital[0:1]
				digit2 = digital[1:2]
				digit3 = digital[2:3]
				digit4 = digital[3:4]
				digit5 = digital[4:5]
				digit6 = digital[5:6]
				digit7 = digital[6:7]
			if len(digital) == 6:
				digit2 = digital[0:1]
				digit3 = digital[1:2]
				digit4 = digital[2:3]
				digit5 = digital[3:4]
				digit6 = digital[4:5]
				digit7 = digital[5:6]
			if len(digital) == 5:
				digit3 = digital[0:1]
				digit4 = digital[1:2]
				digit5 = digital[2:3]
				digit6 = digital[3:4]
				digit7 = digital[4:5]
			if len(digital) == 4:
				digit4 = digital[0:1]
				digit5 = digital[1:2]
				digit6 = digital[2:3]
				digit7 = digital[3:4]
			if len(digital) == 3:
				digit5 = digital[0:1]
				digit6 = digital[1:2]
				digit7 = digital[2:3]

# Connect RFID reader #
		if operating_mode == 'real':
			realtag = 'None'

			HOST = '192.41.170.55' # CSIM network
#			HOST = '192.168.101.55' # Likitomi network
#			HOST = '192.168.1.55' # My own local network: Linksys
#			HOST = '192.168.2.88' # In Likitomi factory
			PORT = 50007
			soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			soc.settimeout(2)
			soc.connect((HOST, PORT))
			## soc.send('setup.operating_mode = standby\r\n')
			soc.send('tag.db.scan_tags(1000)\r\n')
			datum = soc.recv(128)

			if datum.find("ok") > -1:
				soc.send('tag.read_id()\r\n')
				data = soc.recv(8192)
				tagdata = data.split("\r\n")

			idlist = list()
			loclist = list()

			for tag in tagdata:
#				if "AAAA" in tag:
#					idlist.append(tag)
#				if "BBBB" in tag:
#					loclist.append(tag)
				if "type=STG" in tag or "AAAA" in tag:
					idlist.append(tag)
				if "type=ISOC" and "AAAA" not in tag or "BBBB" in tag:
					loclist.append(tag)

			cnt = 0

			tagid_A = list()
			type_A = list()
			antenna_A = list()
			repeat_A = list()

			for id1 in idlist:
				id2 = id1.replace("(","")
				id2 = id2.replace(")","")
				id3 = id2.split(", ")
				for id4 in id3:
					id5 = id4.split("=")
					if id5[0]=="tag_id":tagid_A.append(id5[1])
					elif id5[0]=="type":type_A.append(id5[1])
					elif id5[0]=="antenna": antenna_A.append(id5[1])
					elif id5[0]=="repeat": repeat_A.append(id5[1])
					cnt= cnt+1

			tagid_B = list()
			type_B = list()
			antenna_B = list()
			repeat_B = list()

			for loc1 in loclist:
				loc2 = loc1.replace("(","")
				loc2 = loc2.replace(")","")
				loc3 = loc2.split(", ")
				for loc4 in loc3 :
					loc5 = loc4.split("=")
					if loc5[0]=="tag_id": tagid_B.append(loc5[1])
					elif loc5[0]=="type": type_B.append(loc5[1])
					elif loc5[0]=="antenna": antenna_B.append(loc5[1])
					elif loc5[0]=="repeat": repeat_B.append(loc5[1])
					cnt= cnt+1

			repeat_AA = list()

			for rep_A in repeat_A:
				repeat_AA.append(int(rep_A))

			if max(repeat_AA) in repeat_AA:
				n = repeat_AA.index(max(repeat_AA))

#			tagsplt = tagid_A[n].split("AAAA")
#			realtag = int(tagsplt[1][0:4])
			realtag = tagid_A[n][7:11]

			soc.close()

		if operating_mode == 'fake':

			realtag = '0067'

# Query database #
		if realtag != 'None':
			query1 = PaperRoll.objects.filter(id=realtag).values_list('paper_code', 'width', 'wunit', 'initial_weight', 'lane', 'position')[0]

			paper_code = query1[0]
			size = query1[1]
			uom = query1[2]
			initial_weight = query1[3]
			lane = query1[4]
			position = query1[5]

			query2 = PaperHistory.objects.filter(roll_id=realtag).order_by('-timestamp').values_list('last_wt')
			exists = PaperHistory.objects.filter(roll_id=realtag).exists()

			int_weight = int(weight)

			if exists == True:
				actual_wt = int(list(query2)[0][0])
			else:
				actual_wt = initial_weight

			if weight != 'None':
				used_weight = actual_wt - int(weight)

# Update temp_weight to database #
				p = PaperRoll(id=realtag, paper_code=paper_code, width=size, wunit=uom, initial_weight=initial_weight, temp_weight=int_weight, lane=lane, position=position)
				p.save()
			else:
				used_weight = ""

# Exceptions #
	except serial.SerialException:
		realtag = ""
		paper_code = ""
		size = ""
		uom = ""
		actual_wt = ""
		used_weight = ""
		serror = "[Please check serial port connection.]"
		return render_to_response('scale.html', locals())

	except OSError:
		realtag = ""
		paper_code = ""
		size = ""
		uom = ""
		actual_wt = ""
		used_weight = ""
		serror = "[Serial port may conflict.]"
		return render_to_response('scale.html', locals())

	except ValueError:
		realtag = ""
		paper_code = ""
		size = ""
		uom = ""
		actual_wt = ""
		used_weight = ""
		socror = "[No ID tag in field.]"
		return render_to_response('scale.html', locals())

	except UnboundLocalError:
		realtag = ""
		paper_code = ""
		size = ""
		uom = ""
		actual_wt = ""
		used_weight = ""
		socror = "[Please change operating mode to 'standby'.]"
		return render_to_response('scale.html', locals())

	except IndexError:
		realtag = ""
		paper_code = ""
		size = ""
		uom = ""
		actual_wt = ""
		used_weight = ""
		socror = "[Please change operating mode to 'standby'.]"
		return render_to_response('scale.html', locals())

	return render_to_response('scale.html', locals())

