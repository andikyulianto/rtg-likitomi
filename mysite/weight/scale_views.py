# Create your views here.
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.template import Template, Context
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.db import connection, transaction

import datetime
import serial
import MySQLdb
import Image
import socket
import StringIO
import cStringIO
import random

def scale(request):
# Connect serial port #
	try:
		weight = 'None'

#		ser = serial.Serial()
#		ser.port = '/dev/ttyUSB0'
#		ser.baudrate = 2400
#		ser.bytesize = 7
#		ser.parity = 'E'
#		ser.stopbits = 1
#		ser.timeout = 2
#		ser.open()
#		ser.flushInput()
#		output = ser.readline()
		output = "US,NT,+00325.5Kg\r\n"
#		ser.close()
		a = output.rsplit(",")
		if len(a) == 3:
			if a[0] == 'US':
				b = a[2]
				if b[0:1] == '+':
					c = b[-11:]
					d = c[:-4]
					weight = float(d)
#					weight = round(random.uniform(1,2000),0)
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

# Connect RFID reader #
		realtag = 'None'

#		HOST = '192.41.170.55' # CSIM network
#		HOST = '192.168.101.55' # Likitomi network
		HOST = '192.168.1.55' # My own local network: Linksys
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
			if "AAAA" in tag:
				idlist.append(tag)
			if "BBBB" in tag:
				loclist.append(tag)

		cnt = 0
		## error = cStringIO.StringIO()

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

		tagsplt = tagid_A[n].split("AAAA")
		realtag = int(tagsplt[1][0:4])

		soc.close()

#		realtag = 68

# Query database #
		if realtag != 'None':
			conn = MySQLdb.Connect(host="localhost", user="root", passwd="", db="likitomi_v8")
			cur = conn.cursor()
			cur.execute("SELECT * FROM `paper_rolldetails` WHERE `paper_rolldetails`.`paper_roll_detail_id` = %s LIMIT 1", realtag)
			query1 = cur.fetchone()
			paper_roll_id = query1[0]
			paper_code = query1[1]
			initial_weight = query1[4]
			size = query1[7]
			uom = query1[8]

			cur.execute("SELECT * FROM `paper_movement` WHERE `paper_movement`.`roll_id` = %s ORDER BY `paper_movement`.`created_on` DESC", realtag)
			query2 = cur.fetchall()

			if len(query2)>0:
				actual_wt = query2[0][3]
			else:
				actual_wt = initial_weight

			if weight != 'None':
				used_weight = actual_wt - weight

# Update temp_weight to database #
				cur.execute("UPDATE `likitomi_v8`.`paper_rolldetails` SET `temp_weight` = %s WHERE `paper_rolldetails`.`paper_roll_detail_id` = %s", (weight, realtag))
				conn.commit()

				cur.close()
				conn.close()
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

	return render_to_response('scale.html', locals())

