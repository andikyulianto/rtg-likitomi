# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.db import connection, transaction
from weight.models import PaperRolldetails, PaperMovement

def tagman(request):
	tagiddomain = range(1,10000)
	tagidquery = PaperRolldetails.objects.values_list('paper_roll_detail_id')
	tagidlist = PaperRolldetails.objects.values_list('paper_roll_detail_id', flat=True).order_by('-paper_roll_detail_id')
	for tag in tagidlist:
		if tag in tagiddomain: tagiddomain.remove(tag)
	avaitag = tagiddomain[0]

	spcode = PaperRolldetails.objects.values_list('paper_code').distinct().order_by('paper_code')
	spcodelist = list()
	for pcode in spcode:
		spcodelist.append(pcode[0])

	swidth = PaperRolldetails.objects.values_list('size').distinct().order_by('size')
	swidthlist = list()
	for width in swidth:
		swidthlist.append(width[0])

	query = PaperRolldetails.objects.values_list('paper_roll_detail_id', 'rfid_roll_id', 'paper_code', 'size', 'initial_weight', 'lane', 'position').order_by('rfid_roll_id','paper_roll_detail_id')

	qlist = list(query)
	nlist = list()
	for lst in qlist:
		nlst = list(lst)
		nlist.append(nlst)

	for lst in nlist:
		roll_id = lst[0]
		if PaperMovement.objects.filter(roll_id=roll_id).exists() == True:
			current_weight = int(PaperMovement.objects.filter(roll_id=roll_id).order_by('-created_on')[0].actual_wt)
		else:
			current_weight = PaperRolldetails.objects.get(paper_roll_detail_id=roll_id).initial_weight
		lst.append(current_weight)

	return render_to_response('tagman.html', locals())

def showtaglist(request):
	tagiddomain = range(1,10000)
	tagidquery = PaperRolldetails.objects.values_list('paper_roll_detail_id')
	tagidlist = PaperRolldetails.objects.values_list('paper_roll_detail_id', flat=True).order_by('-paper_roll_detail_id')
	for tag in tagidlist:
		if tag in tagiddomain: tagiddomain.remove(tag)
	avaitag = tagiddomain[0]

	spcode = PaperRolldetails.objects.values_list('paper_code').distinct().order_by('paper_code')
	spcodelist = list()
	for pcode in spcode:
		spcodelist.append(pcode[0])

	swidth = PaperRolldetails.objects.values_list('size').distinct().order_by('size')
	swidthlist = list()
	for width in swidth:
		swidthlist.append(width[0])

	query = PaperRolldetails.objects.values_list('paper_roll_detail_id', 'rfid_roll_id', 'paper_code', 'size', 'initial_weight', 'lane', 'position').order_by('rfid_roll_id','paper_roll_detail_id')

	qlist = list(query)
	nlist = list()
	for lst in qlist:
		nlst = list(lst)
		nlist.append(nlst)

	for lst in nlist:
		roll_id = lst[0]
		if PaperMovement.objects.filter(roll_id=roll_id).exists() == True:
			current_weight = int(PaperMovement.objects.filter(roll_id=roll_id).order_by('-created_on')[0].actual_wt)
		else:
			current_weight = PaperRolldetails.objects.get(paper_roll_detail_id=roll_id).initial_weight
		lst.append(current_weight)

	return render_to_response('showtaglist.html', locals())

def createnew(request):
	if 'asupid' in request.GET and request.GET['asupid']:
		asupid = request.GET['asupid']

	if 'arollid' in request.GET and request.GET['arollid']:
		arollid = request.GET['arollid']

	if 'arfid' in request.GET and request.GET['arfid']:
		arfid = int(request.GET['arfid'])
		if len(str(arfid)) == 1: strarfid = '000'+str(arfid)
		if len(str(arfid)) == 2: strarfid = '00'+str(arfid)
		if len(str(arfid)) == 3: strarfid = '0'+str(arfid)

	if 'apcode' in request.GET and request.GET['apcode']:
		apcode = request.GET['apcode']

	if 'asize' in request.GET and request.GET['asize']:
		asize = int(request.GET['asize'])

	if 'aweight' in request.GET and request.GET['aweight']:
		aweight = int(request.GET['aweight'])

	if 'alane' in request.GET and request.GET['alane']:
		alane = request.GET['alane']
	else:
		alane = ''

	if 'aposition' in request.GET and request.GET['aposition']:
		aposition = int(request.GET['aposition'])
	else:
		aposition = None

	if 'atag2write' in request.GET and request.GET['atag2write']:
		atag2write = request.GET['atag2write']

	if asupid and arollid and strarfid and apcode and asize and aweight and atag2write:
		if str(strarfid) == str(atag2write[1:5]):
			PaperRolldetails.objects.filter(paper_roll_detail_id=arollid).update(supplier_roll_id=asupid, paper_code=apcode, size=asize, uom='inch', initial_weight=aweight, lane=alane, position=aposition)
		else:
			try:
				HOST = '192.41.170.55' # CSIM network
#				HOST = '192.168.101.55' # Likitomi network
#				HOST = '192.168.1.55' # My own local network: Linksys
#				HOST = '192.168.2.88' # In Likitomi factory
				PORT = 50007
				soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				soc.settimeout(2)
				soc.connect((HOST, PORT))
				soc.send('tag.write_id(new_tag_id=3'+strarfid+'AAAA000000000000000, tag_id='+atag2write+')\r\n')
				response = soc.recv(128)
				soc.close()

				if response.find('ok') != -1:
					if atag2write.count('0') < 15:
						PaperRolldetails.objects.create(paper_roll_detail_id=arollid, rfid_roll_id=arfid, supplier_roll_id=asupid, paper_code=apcode, size=asize, uom='inch', initial_weight=aweight, lane=alane, position=aposition)
					if atag2write.count('0') >= 15:
						PaperRolldetails.objects.create(paper_roll_detail_id=arollid, rfid_roll_id=arfid, supplier_roll_id=asupid, paper_code=apcode, size=asize, uom='inch', initial_weight=aweight, lane=alane, position=aposition)
						tag2del = int(atag2write[1:5])
						PaperRolldetails.objects.filter(paper_roll_detail_id=tag2del).delete()
				else:
					mode = 'min'
					return render_to_response('writagror.html', locals())

			except socket.timeout:
				mode = 'min'
				socror = 'Cannot connect to RFID reader'
				return render_to_response('socror.html', locals())

	return HttpResponseRedirect('/django/tagman/')

def assigntag(request):
#	if 'asupid' in request.GET and request.GET['asupid']:
#		asupid = request.GET['asupid']

#	if 'arollid' in request.GET and request.GET['arollid']:
#		arollid = request.GET['arollid']

	if 'arfid' in request.GET and request.GET['arfid']:
		arfid = int(request.GET['arfid'])
		if len(str(arfid)) == 1: strarfid = '000'+str(arfid)
		if len(str(arfid)) == 2: strarfid = '00'+str(arfid)
		if len(str(arfid)) == 3: strarfid = '0'+str(arfid)

#	if 'apcode' in request.GET and request.GET['apcode']:
#		apcode = request.GET['apcode']

#	if 'asize' in request.GET and request.GET['asize']:
#		asize = int(request.GET['asize'])

#	if 'aweight' in request.GET and request.GET['aweight']:
#		aweight = int(request.GET['aweight'])

	if 'alane' in request.GET and request.GET['alane']:
		alane = request.GET['alane']
	else:
		alane = ''

	if 'aposition' in request.GET and request.GET['aposition']:
		aposition = int(request.GET['aposition'])
	else:
		aposition = None

	if 'atag2write' in request.GET and request.GET['atag2write']:
		atag2write = request.GET['atag2write']

	if strarfid and atag2write:
		if str(strarfid) == str(atag2write[1:5]):
			PaperRolldetails.objects.filter(paper_roll_detail_id=arfid).update(lane=alane, position=aposition)
		else:
			try:
				HOST = '192.41.170.55' # CSIM network
#				HOST = '192.168.101.55' # Likitomi network
#				HOST = '192.168.1.55' # My own local network: Linksys
#				HOST = '192.168.2.88' # In Likitomi factory
				PORT = 50007
				soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				soc.settimeout(2)
				soc.connect((HOST, PORT))
				soc.send('tag.write_id(new_tag_id=3'+strarfid+'AAAA000000000000000, tag_id='+atag2write+')\r\n')

				response = soc.recv(128)
				soc.close()

				if response.find('ok') != -1:
					PaperRolldetails.objects.filter(paper_roll_detail_id=arfid).update(rfid_roll_id=arfid)
#					if atag2write.count('0') < 15:
#						PaperRolldetails.objects.create(paper_roll_detail_id=arollid, rfid_roll_id=arfid, supplier_roll_id=asupid, paper_code=apcode, size=asize, uom='inch', initial_weight=aweight, lane=alane, position=aposition)
#					if atag2write.count('0') >= 15:
#						PaperRolldetails.objects.create(paper_roll_detail_id=arollid, rfid_roll_id=arfid, supplier_roll_id=asupid, paper_code=apcode, size=asize, uom='inch', initial_weight=aweight, lane=alane, position=aposition)
#						tag2del = int(atag2write[1:5])
#						PaperRolldetails.objects.filter(paper_roll_detail_id=tag2del).delete()
				else:
					mode = 'min'
					return render_to_response('writagror.html', locals())

			except socket.timeout:
				mode = 'min'
				socror = 'Cannot connect to RFID reader'
				return render_to_response('socror.html', locals())

	return HttpResponseRedirect('/django/tagman/')

def writemore(request):
#	if 'asupid' in request.GET and request.GET['asupid']:
#		asupid = request.GET['asupid']

#	if 'arollid' in request.GET and request.GET['arollid']:
#		arollid = request.GET['arollid']

	if 'arfid' in request.GET and request.GET['arfid']:
		arfid = int(request.GET['arfid'])
		if len(str(arfid)) == 1: strarfid = '000'+str(arfid)
		if len(str(arfid)) == 2: strarfid = '00'+str(arfid)
		if len(str(arfid)) == 3: strarfid = '0'+str(arfid)

#	if 'apcode' in request.GET and request.GET['apcode']:
#		apcode = request.GET['apcode']

#	if 'asize' in request.GET and request.GET['asize']:
#		asize = int(request.GET['asize'])

#	if 'aweight' in request.GET and request.GET['aweight']:
#		aweight = int(request.GET['aweight'])

#	if 'alane' in request.GET and request.GET['alane']:
#		alane = request.GET['alane']
#	else:
#		alane = ''

#	if 'aposition' in request.GET and request.GET['aposition']:
#		aposition = int(request.GET['aposition'])
#	else:
#		aposition = None

	if 'atag2write' in request.GET and request.GET['atag2write']:
		atag2write = request.GET['atag2write']

	if strarfid and atag2write:
		if str(strarfid) == str(atag2write[1:5]):
			PaperRolldetails.objects.filter(paper_roll_detail_id=arfid).update(lane=alane, position=aposition)
		else:
			try:
				HOST = '192.41.170.55' # CSIM network
#				HOST = '192.168.101.55' # Likitomi network
#				HOST = '192.168.1.55' # My own local network: Linksys
#				HOST = '192.168.2.88' # In Likitomi factory
				PORT = 50007
				soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				soc.settimeout(2)
				soc.connect((HOST, PORT))
				soc.send('tag.write_id(new_tag_id=3'+strarfid+'AAAA000000000000000, tag_id='+atag2write+')\r\n')

				response = soc.recv(128)
				soc.close()

				if response.find('ok') != -1:
					PaperRolldetails.objects.filter(paper_roll_detail_id=arfid).update(rfid_roll_id=arfid)
#					if atag2write.count('0') < 15:
#						PaperRolldetails.objects.create(paper_roll_detail_id=arollid, rfid_roll_id=arfid, supplier_roll_id=asupid, paper_code=apcode, size=asize, uom='inch', initial_weight=aweight, lane=alane, position=aposition)
#					if atag2write.count('0') >= 15:
#						PaperRolldetails.objects.create(paper_roll_detail_id=arollid, rfid_roll_id=arfid, supplier_roll_id=asupid, paper_code=apcode, size=asize, uom='inch', initial_weight=aweight, lane=alane, position=aposition)
#						tag2del = int(atag2write[1:5])
#						PaperRolldetails.objects.filter(paper_roll_detail_id=tag2del).delete()
				else:
					mode = 'min'
					return render_to_response('writagror.html', locals())

			except socket.timeout:
				mode = 'min'
				socror = 'Cannot connect to RFID reader'
				return render_to_response('socror.html', locals())

	return HttpResponseRedirect('/django/tagman/')
