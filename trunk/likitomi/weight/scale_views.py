from django.shortcuts import render_to_response
from django.core.cache import cache
import serial
import socket
import random
from datetime import datetime
from weight.models import PaperRoll, PaperHistory

def scale(request):

# Setting scale mode and rfid mode = {'real', 'fake'} #
	scale_mode = 'real'
	rfid_mode = 'fake' 

	if scale_mode == 'real':
# Connect to scale via serial port #
		try:
			ser = serial.Serial()
			ser.port = '/dev/ttyUSB2' # on GNU/Linux
#			ser.port = 'COM3' # on Windows
			ser.baudrate = 2400
			ser.bytesize = 7
			ser.parity = 'E'
			ser.stopbits = 1
			ser.timeout = 2
			ser.open()
			ser.flushInput()
			output = ser.readline()
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

	if rfid_mode == 'real':
# Connect to RFID reader #
		try:
			HOST = '192.41.170.55' # CSIM network
#			HOST = '192.168.101.55' # Likitomi network
#			HOST = '192.168.1.55' # My own local network: Linksys
#			HOST = '192.168.2.88' # In Likitomi factory
			PORT = 50007
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
					cache.set('timestamp', timestamp, 10)
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
				if "BBBB" in tag:
					loclist.append(tag)
				else:
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
						prelindex = tagid_B[cnt][25:27]
						if prelindex == 'AB': lindex = 1
						if prelindex == 'CD': lindex = 2
						if prelindex == 'EF': lindex = 3
						if prelindex == 'FF': lindex = 4
						if prelindex == 'CC': lindex = 0
						if prelindex == 'DD': lindex = 5
						pindex = int(tagid_B[cnt][27:30])
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
					realtag = tagid_A[n][7:11]
					tag2write = tagid_A[n][6:30]

					if tag2write.count('0') < 15 or PaperRoll.objects.filter(tarid=realtag).exists() == False:
						tagstatus = 'unknown'
					elif tag2write.count('0') >= 15:
						tagstatus = 'known'

					if PaperRoll.objects.filter(tarid=realtag).exists() == True:
						query = PaperRoll.objects.get(tarid=realtag)
						paper_code = query.paper_code
						size = query.width
						uom = query.wunit

						int_weight = int(weight)

						if PaperHistory.objects.filter(roll_id=realtag).exists() == True:
							actual_wt = PaperHistory.objects.filter(roll_id=realtag).order_by('-timestamp')[0].last_wt
						else:
							actual_wt = query.initial_weight

						used_weight = actual_wt - int(weight)

						PaperRoll.objects.filter(tarid=realtag).update(temp_weight=int_weight)

	if rfid_mode == 'fake':

#		tag2write = '112233445566778899AABBCC'
		tag2write = '30065AAAA000000000000000'
		realtag = tag2write[1:5]

		if tag2write.count('0') < 15 or PaperRoll.objects.filter(tarid=realtag).exists() == False:
			tagstatus = 'unknown'
		elif tag2write.count('0') >= 15:
			tagstatus = 'known'
		lasttime = datetime.now().strftime("%H:%M:%S")

		if PaperRoll.objects.filter(tarid=realtag).exists() == True:
			query = PaperRoll.objects.get(tarid=realtag)
			paper_code = query.paper_code
			size = query.width
			uom = query.wunit

			if PaperHistory.objects.filter(roll_id=realtag).exists() == True:
				actual_wt = PaperHistory.objects.filter(roll_id=realtag).order_by('-timestamp')[0].last_wt
			else:
				actual_wt = query.initial_weight

			if not serror:
				int_weight = int(weight)
				used_weight = actual_wt - int(weight)

				PaperRoll.objects.filter(tarid=realtag).update(temp_weight=int_weight)

	return render_to_response('scale.html', locals())

