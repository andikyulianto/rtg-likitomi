from django.shortcuts import render_to_response
from django.core.cache import cache
from datetime import datetime
import sys
import random

import serial
import socket

from weight.models import PaperRolldetails, PaperMovement

# HOST and PORT settings for RFID reader connection
HOST = '192.168.2.88' # Likitomi's factory
PORT = 50007

def scale(request):
	"""
	Views of scale application.

		Connect and retrieve the weight from weighing indicator via serial port.

		Connect and retrieve the paper roll tag information from RFID reader.

		Update the temporary weight of a particular paper roll.

	**Context:**

	``Models``

		:model:`weight.PaperRolldetails`

		:model:`weight.PaperMovement`

	``Special Modules``

		serial: For making a connection to weighing indicator.

		socket: For making a connection to RFID reader.

	**Template:**

	:template:`templates/clamplift/scale.html`

	"""

# Setting scale mode and rfid mode = {'real', 'fake'}
	scale_mode = 'real'
	rfid_mode = 'real'

# Connect to scale via serial port
	if scale_mode == 'real':
		try:
			ser = serial.Serial()
			ser.baudrate = 2400
			ser.bytesize = 7
			ser.parity = 'E'
			ser.stopbits = 1
			ser.timeout = 2
			if sys.platform == 'linux2': # on GNU/Linux
				for i in range(8):
					try:
						ser.port = '/dev/ttyUSB'+str(i)
						ser.open()
						ser.flushInput()
						output = ser.readline()
					except:
						serror = "Cannot connect to scale"
			if sys.platform == 'win32': # on Windows
				for i in range(8):
					try:
						ser.port = 'COM'+str(i)
						ser.open()
						ser.flushInput()
						output = ser.readline()
					except:
						serror = "Cannot connect to scale"
			ser.close()
		except serial.SerialException:
			serror = "Cannot connect to scale"

		if not serror:
			if output:
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
#								digit6 = digital[5:6]
#								digit7 = digital[6:7]
							if len(digital) == 6:
								digit2 = digital[0:1]
								digit3 = digital[1:2]
								digit4 = digital[2:3]
								digit5 = digital[3:4]
#								digit6 = digital[4:5]
#								digit7 = digital[5:6]
							if len(digital) == 5:
								digit3 = digital[0:1]
								digit4 = digital[1:2]
								digit5 = digital[2:3]
								digit6 = digital[3:4]
#								digit7 = digital[4:5]
#							if len(digital) == 4:
								digit4 = digital[0:1]
								digit5 = digital[1:2]
#								digit6 = digital[2:3]
#								digit7 = digital[3:4]
							if len(digital) == 3:
								digit5 = digital[0:1]
#								digit6 = digital[1:2]
#								digit7 = digital[2:3]
						else:
							serror = "Negative value"
					else:
						serror = "Overload value"
				else:
					serror = "Incomplete data"
			else:
				serror = "No data received"

	if scale_mode == 'fake': # Fake mode just for running application without weighing indicator
		output = "US,NT,+00325.5Kg\r\n"
#		weight = round(random.uniform(1,500),0)
		weight = 482.0
		digital = str(weight)
		if len(digital) == 7:
			digit1 = digital[0:1]
			digit2 = digital[1:2]
			digit3 = digital[2:3]
			digit4 = digital[3:4]
			digit5 = digital[4:5]
#			digit6 = digital[5:6]
#			digit7 = digital[6:7]
		if len(digital) == 6:
			digit2 = digital[0:1]
			digit3 = digital[1:2]
			digit4 = digital[2:3]
			digit5 = digital[3:4]
#			digit6 = digital[4:5]
#			digit7 = digital[5:6]
		if len(digital) == 5:
			digit3 = digital[0:1]
			digit4 = digital[1:2]
			digit5 = digital[2:3]
#			digit6 = digital[3:4]
#			digit7 = digital[4:5]
		if len(digital) == 4:
			digit4 = digital[0:1]
			digit5 = digital[1:2]
#			digit6 = digital[2:3]
#			digit7 = digital[3:4]
		if len(digital) == 3:
			digit5 = digital[0:1]
#			digit6 = digital[1:2]
#			digit7 = digital[2:3]

# Connect to RFID reader
	if rfid_mode == 'real':
		try:
			soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			soc.settimeout(2)
			soc.connect((HOST, PORT))
			## soc.send('setup.operating_mode = standby\r\n')
			soc.send('tag.db.scan_tags(100)\r\n')
			datum = soc.recv(32)
			if datum.find("ok") > -1:
				soc.send('tag.read_id()\r\n')
				recv = soc.recv(8192)
				if recv.find("tag_id") > -1:
					cache.set('data', recv, 10) # Wait 10 seconds for 'data' to expire...
					timestamp = datetime.now().strftime("%H:%M:%S")
					cache.set('timestamp', timestamp, 10) # Wait 10 seconds for 'timestamp' to expire...
			soc.close()
		except socket.timeout:
			socror = 'Cannot connect to RFID reader'

		data = cache.get('data')
		lasttime = cache.get('timestamp')
		tagdata = str(data).split("\r\n")

		if len(tagdata) > 0:
			idlist = list()
			loclist = list()

			for tag in tagdata:
				if "3000000000000000000" in tag: # Pattern of location tag
					loclist.append(tag)
				else: # This will append both paper roll ID tag and new (unknown) tag into "idlist"
					idlist.append(tag)

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
					cnt = cnt+1

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
					cnt = cnt+1

			lan = 0
			pos = 0
			totalCount = 0

			if len(repeat_B) > 0 :
				cnt = 0
				for rep in repeat_B:
					if type_B[cnt] == "ISOC":
						prelindex = tagid_B[cnt][21:23]
						if prelindex == 'AB': lindex = 1
						if prelindex == 'CD': lindex = 2
						if prelindex == 'EF': lindex = 3
						if prelindex == 'FF': lindex = 4
						if prelindex == 'CC': lindex = 0
						if prelindex == 'DD': lindex = 5
						pindex = int(tagid_B[cnt][23:26])
						lan += float(lindex)*float(repeat_B[cnt])
						pos += float(pindex)*float(repeat_B[cnt])
						totalCount += float(repeat_B[cnt])

					cnt = cnt+1

			if totalCount > 0:
				L = int(round(lan/totalCount,0))
				P = int(round(pos/totalCount,0))
			else:
				L = 0
				P = 0

			atlane = str(L)
			atposition = str(P)
			atlocation = ''

			if L == 0:
				atlocation = 'CR'
			if L == 5:
				atlocation = 'Scale'
			if L in range(1, 5):
				atlocation = 'Stock'

			if L == 0 and P == 0:
				atlane = ""
				atposition = ""
				atlocation = ""

			repeat_AA = list()

			for rep_A in repeat_A:
				repeat_AA.append(int(rep_A))

			if len(repeat_AA) > 0:
				if max(repeat_AA) in repeat_AA:
					n = repeat_AA.index(max(repeat_AA))
					realtag = tagid_A[n][16:30]
					tag2write = tagid_A[n][2:30]

					if tag2write.find('30000000000000') == -1 or PaperRolldetails.objects.filter(likitomi_roll_id=realtag).exists() == False:
						tagstatus = 'unknown'
					elif tag2write.find('30000000000000') == 0:
						tagstatus = 'known'

					if realtag and PaperRolldetails.objects.filter(likitomi_roll_id=realtag).exists() == True:
						query = PaperRolldetails.objects.get(likitomi_roll_id=realtag)
						paper_code = query.paper_code
						size = query.size
						uom = query.uom

						int_weight = int(weight)

						if PaperMovement.objects.filter(roll_id=realtag).exists() == True:
							actual_wt = int(PaperMovement.objects.filter(roll_id=realtag).order_by('-created_on')[0].actual_wt)
						else:
							actual_wt = query.initial_weight

						used_weight = actual_wt - int(weight)

# Update the weight from weighing indicator as temporary weight of the paper roll
						PaperRolldetails.objects.filter(likitomi_roll_id=realtag).update(temp_weight=int_weight)

	if rfid_mode == 'fake': # Fake mode just for running application without weighing indicator

#		tag2write = '112233445566778899AABBCC'
		tag2write = '300000000000005408090065'
		realtag = tag2write[14:24]

		lasttime = datetime.now().strftime("%H:%M:%S")

		if tag2write.find('30000000000000') == -1 or PaperRolldetails.objects.filter(likitomi_roll_id=realtag).exists() == False:
			tagstatus = 'unknown'

		elif tag2write.find('30000000000000') == 0:
			tagstatus = 'known'

		if realtag and PaperRolldetails.objects.filter(likitomi_roll_id=realtag).exists() == True:
			query = PaperRolldetails.objects.get(likitomi_roll_id=realtag)
			paper_code = query.paper_code
			size = query.size
			uom = query.uom

			if PaperMovement.objects.filter(roll_id=realtag).exists() == True:
				actual_wt = int(PaperMovement.objects.filter(roll_id=realtag).order_by('-created_on')[0].actual_wt)
			else:
				actual_wt = query.initial_weight

			if weight:
				int_weight = int(weight)
				used_weight = actual_wt - int(weight)

				PaperRolldetails.objects.filter(likitomi_roll_id=realtag).update(temp_weight=int_weight)

	return render_to_response('scale.html', locals())

