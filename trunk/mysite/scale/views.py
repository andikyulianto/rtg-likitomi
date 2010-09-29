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

def weight(request):
# Connect serial port #
##    try:
##        ser = serial.Serial()
##        ser.port = 3 # COM4
##        ser.baudrate = 2400
##        ser.bytesize = 7
##        ser.parity = 'E'
##        ser.stopbits = 1
##        ser.timeout = 1
##        ser.open()
##    except serial.SerialException:
##        realtag = ""
##        paper_code = ""
##        current_weight = ""
##        used_weight = ""
##        error1 = "Serial port communication error!"
##        return render_to_response('weight2.html', locals())
##
##    output = ser.read(16)

    output = "US,NT,+00234.5Kg"

    a = output.rsplit(",")

    if len(a) == 3:
        b = a[2]
    elif len(a) == 2:
        b = a[1]
    else:
        b = "+00000.0Kg"

    if len(b) == 10:
        c = b[-9:]
    else:
        c = "00000.0Kg"

    if len(c) == 9:
        d = c[:-2]
    else:
        d = "00000.0"

    weight = float(d)

    if weight != 0.0:
        digital = str(weight)
    else:
        digital = ""
        error2 = "Loading..."

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

##    ser.close()

# Connect RFID reader #
    HOST = '192.41.170.55'
    PORT = 50007
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
        error = cStringIO.StringIO()

        tagid_A = list()
        type_A = list()
        antenna_A = list()
        repeat_A = list()

        for id1 in idlist:
            id2 = id1.replace("(","")
            id2 = id2.replace(")","")
            id3 = id2.split(", ")
            for id4 in id3:
                try:
    				id5 = id4.split("=")
    				if id5[0]=="tag_id":tagid_A.append(id5[1])
    				elif id5[0]=="type":type_A.append(id5[1])
    				elif id5[0]=="antenna": antenna_A.append(id5[1])
    				elif id5[0]=="repeat": repeat_A.append(id5[1])
    				cnt= cnt+1
                except IndexError:
    				error.write('%d, ' % cnt)

        tagid_B = list()
        type_B = list()
        antenna_B = list()
        repeat_B = list()

        for loc1 in loclist:
            loc2 = loc1.replace("(","")
            loc2 = loc2.replace(")","")
            loc3 = loc2.split(", ")
            for loc4 in loc3 :
                try:
    				loc5 = loc4.split("=")
    				if loc5[0]=="tag_id": tagid_B.append(loc5[1])
    				elif loc5[0]=="type": type_B.append(loc5[1])
    				elif loc5[0]=="antenna": antenna_B.append(loc5[1])
    				elif loc5[0]=="repeat": repeat_B.append(loc5[1])
    				cnt= cnt+1
                except IndexError:
    				error.write('%d, ' % cnt)

        repeat_AA = list()
        for rep_A in repeat_A:
            repeat_AA.append(int(rep_A))

        try:
            if max(repeat_AA) in repeat_AA:
                n = repeat_AA.index(max(repeat_AA))
            tagsplt = tagid_A[n].split("AAAA")
            realtag = tagsplt[1][0:4]
        except ValueError:
            realtag = ""
            paper_code = ""
            current_weight = ""
            used_weight = ""
            error3 = "No ID tag in field."
            return render_to_response('weight2.html', locals())

    soc.close()

##    realtag = '0065'

# Query database #
    conn = MySQLdb.Connect(host="localhost", user="root", passwd="", db="scale")
    cur = conn.cursor()

    cur.execute("SELECT * FROM `scale_stock` WHERE `scale_stock`.`paper_roll_id` = %s LIMIT 1", realtag)
    query1 = cur.fetchone()
    paper_roll_id = query1[0]
    paper_code = query1[1]
    initial_weight = query1[2]

    cur.execute("SELECT * FROM `scale_movement` WHERE `scale_movement`.`paper_roll_id` = %s ORDER BY `scale_movement`.`up_datetime` DESC", realtag)
    query2 = cur.fetchall()
    if len(query2)>0:
        to_weight = query2[0][3]
    else:
        to_weight = initial_weight
    used_weight = to_weight - weight

# Update temp_weight to database #
    cur.execute("UPDATE `scale`.`scale_stock` SET `temp_weight` = %s WHERE `scale_stock`.`paper_roll_id` = %s", (weight, realtag))
    conn.commit()

    cur.close()
    conn.close()

    return render_to_response('weight2.html', locals())

#-##--###--##-#-##--###--##-#-##--###--##-#-##--###--##-#-##--###--##-#-##--###--##-#-##--###--##-#-##--###--##-#-##--###--##-#-##--###--##-#
#-##--###--##-#-##--###--##-#-##--###--##-#-##--###--##-#-##--###--##-#-##--###--##-#-##--###--##-#-##--###--##-#-##--###--##-#-##--###--##-#
#-##--###--##-#-##--###--##-#-##--###--##-#-##--###--##-#-##--###--##-#-##--###--##-#-##--###--##-#-##--###--##-#-##--###--##-#-##--###--##-#

def clamplift(request):
# Connect RFID reader #
    HOST = '192.41.170.55'
    PORT = 50007
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
        error = cStringIO.StringIO()

        tagid_A = list()
        type_A = list()
        antenna_A = list()
        repeat_A = list()

        for id1 in idlist:
            id2 = id1.replace("(","")
            id2 = id2.replace(")","")
            id3 = id2.split(", ")
            for id4 in id3:
                try:
    				id5 = id4.split("=")
    				if id5[0]=="tag_id":tagid_A.append(id5[1])
    				elif id5[0]=="type":type_A.append(id5[1])
    				elif id5[0]=="antenna": antenna_A.append(id5[1])
    				elif id5[0]=="repeat": repeat_A.append(id5[1])
    				cnt= cnt+1
                except IndexError:
    				error.write('%d, ' % cnt)

        tagid_B = list()
        type_B = list()
        antenna_B = list()
        repeat_B = list()

        for loc1 in loclist:
            loc2 = loc1.replace("(","")
            loc2 = loc2.replace(")","")
            loc3 = loc2.split(", ")
            for loc4 in loc3 :
                try:
    				loc5 = loc4.split("=")
    				if loc5[0]=="tag_id": tagid_B.append(loc5[1])
    				elif loc5[0]=="type": type_B.append(loc5[1])
    				elif loc5[0]=="antenna": antenna_B.append(loc5[1])
    				elif loc5[0]=="repeat": repeat_B.append(loc5[1])
    				cnt= cnt+1
                except IndexError:
    				error.write('%d, ' % cnt)

        repeat_AA = list()
        for rep_A in repeat_A:
            repeat_AA.append(int(rep_A))

        try:
            if max(repeat_AA) in repeat_AA:
                n = repeat_AA.index(max(repeat_AA))
            tagsplt = tagid_A[n].split("AAAA")
            realtag = tagsplt[1][0:4]
        except ValueError:
            realtag = ""
            paper_code = ""
            lane = ""
            position = ""
            location = ""
            to_weight = ""
            error3 = "No ID tag in field."
            return render_to_response('clamplift.html', locals())

        lan = 0
        pos = 0
        totalCount = 0
        if len(repeat_B) > 0 :
    		cnt = 0
    		for rep in repeat_B:
    			try:
    				if type_B[cnt] == "ISOC":
    					lindex = int(tagid_B[cnt][26:28])
    					pindex = int(tagid_B[cnt][28:30])
    					lan += float(lindex)*float(repeat_B[cnt])
    					pos += float(pindex)*float(repeat_B[cnt])
    					totalCount += float(repeat_B[cnt])

    			except IndexError:
    				break;
    			cnt = cnt+1

        if totalCount > 0:
    		L = int(round(lan/totalCount,0))
    		P = int(round(pos/totalCount,0))
        else:
            L = 0
            P = 0

        lane = str(L)
        position = str(P)

        if L == 1 and P == 10:
            location = 'CR'
        if L == 1 and P == 11:
            location = 'Scale'
        if L == 1 and P == 12:
            location = 'Stock'

        if L == 0 and P == 0:
            lane = ""
            position = ""
            error4 = "No location tag in field."

    soc.close()

##    realtag = '0069'
##    lane = '4'
##    position = '43'

# Query database #
    conn = MySQLdb.Connect(host="localhost", user="root", passwd="", db="scale")
    cur = conn.cursor()

    cur.execute("SELECT * FROM `scale_stock` WHERE `scale_stock`.`paper_roll_id` = %s", realtag)
    query1 = cur.fetchone()
    paper_roll_id = query1[0]
    paper_code = query1[1]
    initial_weight = query1[2]
    temp_weight = query1[3]

    cur.execute("SELECT * FROM `scale_movement` WHERE `scale_movement`.`paper_roll_id` = %s ORDER BY `scale_movement`.`up_datetime` DESC", realtag)
    query2 = cur.fetchall()
    if len(query2)>0:
        to_weight = query2[0][3]
    else:
        to_weight = initial_weight

##    leng = len(query2)
##    length = 0
##    up_datetime_list = list()
##    to_weight_list = list()
##    while (length < len(query2)):
##        up_datetime_list.append(query2[length][4].strftime("%d-%m-%Y %H:%M:%S"))
##        to_weight_list.append(query2[length][3])
##        length = length + 1

    cur.close()
    conn.close()

    return render_to_response('clamplift.html', locals())

# Update weight to database #
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

    conn = MySQLdb.Connect(host="localhost", user="root", passwd="", db="scale")
    cur = conn.cursor()
    cur.execute("SELECT * FROM `scale_stock` WHERE `scale_stock`.`paper_roll_id` = %s LIMIT 1", realtag)

    query1 = cur.fetchone()
    paper_roll_id = query1[0]
    paper_code = query1[1]
    initial_weight = query1[2]
    temp_weight = query1[3]

    cur.execute("SELECT * FROM `scale_movement` WHERE `scale_movement`.`paper_roll_id` = %s ORDER BY `scale_movement`.`up_datetime` DESC LIMIT 1", realtag)
    query2 = cur.fetchall()
    if len(query2)>0:
        from_weight = query2[0][3]
    else:
        from_weight = initial_weight

##    cur.execute("UPDATE `scale`.`scale_rollback` SET `current_weight` = %s WHERE `scale_rollback`.`paper_roll_id` = %s", (current_weight, realtag))
##    cur.execute("UPDATE `scale`.`scale_stock` SET `current_weight` = %s WHERE `scale_stock`.`paper_roll_id` = %s", (weight, realtag))

    rightnow = datetime.datetime.now()
    dt = rightnow.strftime("%Y-%m-%d %H:%M:%S")

    cur.execute("INSERT INTO `scale`.`scale_movement` (paper_roll_id, from_weight, to_weight, up_datetime) VALUES (%s, %s, %s, %s)", (realtag, from_weight, weight, dt))
    conn.commit()

    cur.close()
    conn.close()

    return HttpResponseRedirect('/clamplift/')

def undo(request):
    if 'realtag' in request.GET and request.GET['realtag']:
        realtag = request.GET['realtag']
    else:
        return HttpResponseRedirect('/clamplift/')

    conn = MySQLdb.Connect(host="localhost", user="root", passwd="", db="scale")
    cur = conn.cursor()
    cur.execute("SELECT * FROM `scale_rollback` WHERE `scale_rollback`.`paper_roll_id` = %s LIMIT 1", realtag)

    query = cur.fetchone()
    paper_roll_id = query[0]
    paper_code = query[1]
    current_weight = query[2]
    temp_weight = query[3]

##    cur.execute("UPDATE `scale`.`scale_stock` SET `current_weight` = %s WHERE `scale_stock`.`paper_roll_id` = %s", (current_weight, realtag))
    cur.execute("SELECT MAX(up_datetime) FROM `scale`.`scale_movement` WHERE `scale_movement`.`paper_roll_id` = %s", realtag)
    query2 = cur.fetchone()
    max_datetime = query2[0]

    cur.execute("DELETE FROM `scale`.`scale_movement` WHERE `scale_movement`.`paper_roll_id` = %s AND `scale_movement`.`up_datetime` = %s", (realtag, max_datetime))

    conn.commit()

    return HttpResponseRedirect('/clamplift/')

def digit(request):
# Connect RFID reader #
    HOST = '192.41.170.55'
    PORT = 50007
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
        error = cStringIO.StringIO()

        tagid_A = list()
        type_A = list()
        antenna_A = list()
        repeat_A = list()

        for id1 in idlist:
            id2 = id1.replace("(","")
            id2 = id2.replace(")","")
            id3 = id2.split(", ")
            for id4 in id3:
                try:
    				id5 = id4.split("=")
    				if id5[0]=="tag_id":tagid_A.append(id5[1])
    				elif id5[0]=="type":type_A.append(id5[1])
    				elif id5[0]=="antenna": antenna_A.append(id5[1])
    				elif id5[0]=="repeat": repeat_A.append(id5[1])
    				cnt= cnt+1
                except IndexError:
    				error.write('%d, ' % cnt)

        tagid_B = list()
        type_B = list()
        antenna_B = list()
        repeat_B = list()

        for loc1 in loclist:
            loc2 = loc1.replace("(","")
            loc2 = loc2.replace(")","")
            loc3 = loc2.split(", ")
            for loc4 in loc3 :
                try:
    				loc5 = loc4.split("=")
    				if loc5[0]=="tag_id": tagid_B.append(loc5[1])
    				elif loc5[0]=="type": type_B.append(loc5[1])
    				elif loc5[0]=="antenna": antenna_B.append(loc5[1])
    				elif loc5[0]=="repeat": repeat_B.append(loc5[1])
    				cnt= cnt+1
                except IndexError:
    				error.write('%d, ' % cnt)

        repeat_AA = list()
        for rep_A in repeat_A:
            repeat_AA.append(int(rep_A))

        try:
            if max(repeat_AA) in repeat_AA:
                n = repeat_AA.index(max(repeat_AA))
            tagsplt = tagid_A[n].split("AAAA")
            realtag = tagsplt[1][0:4]
        except ValueError:
            digit6 = "-"
            return render_to_response('digit.html', locals())

        soc.close()

##    realtag = '0069'

# Query database #
    conn = MySQLdb.Connect(host="localhost", user="root", passwd="", db="scale")
    cur = conn.cursor()
    cur.execute("SELECT * FROM `scale_stock` WHERE `scale_stock`.`paper_roll_id` = %s LIMIT 1", realtag)

    query = cur.fetchone()
    temp_weight = query[3]

    cur.close()
    conn.close()

    digital = str(temp_weight)

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

    return render_to_response('digit.html', locals())

def test(request):
    return render_to_response('test.html', locals())

# Comments #
# 1. List of previous weight when undo