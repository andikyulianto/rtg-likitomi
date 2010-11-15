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

def clamplift(request):
# Connect RFID reader #
	try:
		HOST = '192.41.170.55' # CSIM network
#		HOST = '192.168.101.55' # Likitomi network
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

		lan = 0
		pos = 0
		totalCount = 0

		if len(repeat_B) > 0 :
			cnt = 0
			for rep in repeat_B:
				if type_B[cnt] == "ISOC":
					lindex = int(tagid_B[cnt][26:28])
					pindex = int(tagid_B[cnt][28:30])
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
		if L == 5 and P == 5:
			atlocation = 'Scale'
		if L in range(1, 5):
			atlocation = 'Stock'

		if L == 0 and P == 0:
			atlane = ""
			atposition = ""
			atlocation = ""
			toperror = "[No location tag in field.]"

		repeat_AA = list()

		for rep_A in repeat_A:
			repeat_AA.append(int(rep_A))

		if max(repeat_AA) in repeat_AA:
			n = repeat_AA.index(max(repeat_AA))

		tagsplt = tagid_A[n].split("AAAA")
		realtag = int(tagsplt[1][0:4])

		soc.close()

#		atlane = 5
#		atposition = 5
#		atlocation = 'Scale'

#		realtag = 68

# Query database #
		conn = MySQLdb.Connect(host="localhost", user="root", passwd="", db="likitomi_v8")
		cur = conn.cursor()

		cur.execute("SELECT * FROM `paper_rolldetails` WHERE `paper_rolldetails`.`paper_roll_detail_id` = %s", realtag)
		query1 = cur.fetchone()
		paper_roll_id = query1[0]
		paper_code = query1[1]
		initial_weight = query1[4]
		size = query1[7]
		uom = query1[8]
		temp_weight = query1[17]
		lane = query1[18]
		position = query1[19]
		uppos = int(position)+1
		downpos = int(position)-1
		digital = str(temp_weight)

		if lane == 'A':
			opplane = 'B'
		if lane == 'B':
			opplane = 'A' 
		if lane == 'C':
			opplane = 'D' 
		if lane == 'D':
			opplane = 'C' 
		if lane == 'E':
			opplane = 'F' 
		if lane == 'F':
			opplane = 'E' 
		if lane == 'G':
			opplane = 'H'
		if lane == 'H':
			opplane = 'G' 

		if atlane == '1':
			leftlane = 'A'
			rightlane = 'B'
		if atlane == '2':
			leftlane = 'C'
			rightlane = 'D'
		if atlane == '3':
			leftlane = 'E'
			rightlane = 'F'
		if atlane == '4':
			leftlane = 'G'
			rightlane = 'H'

		if atlocation != 'Scale':
			wgth_dis = ""
			man_btn = ""
			undo_btn = ""
			submit_btn = ""
			digital = ""

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

		cur.execute("SELECT * FROM `paper_movement` WHERE `paper_movement`.`roll_id` = %s ORDER BY `paper_movement`.`created_on` DESC", realtag)
		query2 = cur.fetchall()

		if len(query2)>0:
			actual_wt = query2[0][3]
		else:
			actual_wt = initial_weight
			undo_btn = ""

		cur.close()
		conn.close()

# Exceptions #
	except UnboundLocalError:
		realtag = ""
		paper_code = ""
		size = ""
		lane = ""
		position = ""
		atlane = ""
		atposition = ""
		atlocation = ""
		actual_wt = ""
		used_weight = ""
		wgth_dis = ""
		man_btn = ""
		undo_btn = ""
		submit_btn = ""
		bottomerror = "[Please change operating mode to 'standby'.]"
		return render_to_response('clamplift.html', locals())

	except ValueError:
		realtag = ""
		paper_code = ""
		size = ""
		lane = ""
		position = ""
#		atlane = ""
#		atposition = ""
#		atlocation = ""
		actual_wt = ""
		wgth_dis = ""
		man_btn = ""
		undo_btn = ""
		submit_btn = ""
		bottomerror = "[No ID tag in field.]"
		return render_to_response('clamplift.html', locals())

	except TypeError:
		realtag = ""
		paper_code = ""
		size = ""
		lane = ""
		position = ""
#		atlane = ""
#		atposition = ""
#		atlocation = ""
		actual_wt = ""
		wgth_dis = ""
		man_btn = ""
		undo_btn = ""
		submit_btn = ""
		bottomerror = "[No ID tag in field.]"
		return render_to_response('clamplift.html', locals())

	except: # Timeout #
		realtag = ""
		paper_code = ""
		size = ""
		lane = ""
		position = ""
		atlane = ""
		atposition = ""
		atlocation = ""
		actual_wt = ""
		used_weight = ""
		wgth_dis = ""
		man_btn = ""
		undo_btn = ""
		submit_btn = ""
		bottomerror = "[Cannot connect RFID reader before timeout.]"
		return render_to_response('clamplift.html', locals())

	return render_to_response('clamplift.html', locals())

###################################################################### UPDATE ######################################################################

@transaction.commit_manually
def update(request):
	if 'weight' in request.GET and request.GET['weight']:
		weight = request.GET['weight']
	else:
		return HttpResponseRedirect('/clamplift/')

	if 'realtag' in request.GET and request.GET['realtag']:
		realtag = request.GET['realtag']
	else:
		return HttpResponseRedirect('/clamplift/')

	conn = MySQLdb.Connect(host="localhost", user="root", passwd="", db="likitomi_v8")
	cur = conn.cursor()

	cur.execute("SELECT * FROM `paper_rolldetails` WHERE `paper_rolldetails`.`paper_roll_detail_id` = %s LIMIT 1", realtag)
	query1 = cur.fetchone()
	paper_roll_id = query1[0]
	paper_code = query1[1]
	initial_weight = query1[4]
	size = query1[7]
	uom = query1[8]
	temp_weight = query1[17]

	cur.execute("SELECT * FROM `paper_movement` WHERE `paper_movement`.`roll_id` = %s ORDER BY `paper_movement`.`created_on` DESC", realtag)
	query2 = cur.fetchall()
	if len(query2)>0:
		actual_wt = query2[0][3]
	else:
		actual_wt = initial_weight

	try:
		f_weight = float(weight)
	except ValueError:
		error = "Your submitted weight is not a number."
		return render_to_response('submit_error.html', locals())

	if actual_wt > f_weight:
		rightnow = datetime.datetime.now()
		dt = rightnow.strftime("%Y-%m-%d %H:%M:%S")
		cur.execute("INSERT INTO `likitomi_v8`.`paper_movement` (roll_id, before_wt, actual_wt, created_on) VALUES (%s, %s, %s, %s)", (realtag, actual_wt, f_weight, dt))
		conn.commit()

	else:
		err = "w"
		error = "Your submitted weight is not less than previous weight."
		return render_to_response('submit_error.html', locals())

	cur.close()
	conn.close()

	return HttpResponseRedirect('/clamplift/')

###################################################################### UNDO ######################################################################

def undo(request):
	if 'realtag' in request.GET and request.GET['realtag']:
		realtag = request.GET['realtag']
	else:
		return HttpResponseRedirect('/clamplift/')

	conn = MySQLdb.Connect(host="localhost", user="root", passwd="", db="likitomi_v8")
	cur = conn.cursor()

	cur.execute("SELECT * FROM `paper_rolldetails` WHERE `paper_rolldetails`.`paper_roll_detail_id` = %s LIMIT 1", realtag)
	query1 = cur.fetchone()
	paper_roll_id = query1[0]
	paper_code = query1[1]
	initial_weight = query1[4]
	size = query1[7]
	uom = query1[8]
	temp_weight = query1[17]

	cur.execute("SELECT MAX(created_on) FROM `likitomi_v8`.`paper_movement` WHERE `paper_movement`.`roll_id` = %s", realtag)
	query2 = cur.fetchone()
	max_datetime = query2[0]

	cur.execute("DELETE FROM `likitomi_v8`.`paper_movement` WHERE `paper_movement`.`roll_id` = %s AND `paper_movement`.`created_on` = %s", (realtag, max_datetime))
	conn.commit()

	return HttpResponseRedirect('/clamplift/')

################################################################## CHANGE LOCATION #################################################################

def changeloc(request):
	if 'realtag' in request.GET and request.GET['realtag']:
		realtag = request.GET['realtag']
	else:
		return HttpResponseRedirect('/clamplift/')

	if 'lane' in request.GET and request.GET['lane']:
		ilane = request.GET['lane']
	else:
		return HttpResponseRedirect('/clamplift/')

	if 'pos' in request.GET and request.GET['pos']:
		ipos = request.GET['pos']
	else:
		return HttpResponseRedirect('/clamplift/')

	if int(ipos) <= 43:
		conn = MySQLdb.Connect(host="localhost", user="root", passwd="", db="likitomi_v8")
		cur = conn.cursor()

		cur.execute("UPDATE `likitomi_v8`.`paper_rolldetails` SET `lane` = %s WHERE `paper_rolldetails`.`paper_roll_detail_id` = %s", (ilane, realtag))
		conn.commit()
		cur.execute("UPDATE `likitomi_v8`.`paper_rolldetails` SET `position` = %s WHERE `paper_rolldetails`.`paper_roll_detail_id` = %s", (ipos, realtag))
		conn.commit()

		cur.close()
		conn.close()
	else:
		err = ""
		error = "Your submitted position is not between 1 and 43."
		return render_to_response('submit_error.html', locals())

	return HttpResponseRedirect('/clamplift/')


################################################################## ORIENTATION #################################################################

def orient(request):
	
	return render_to_response('index2.html', locals())
