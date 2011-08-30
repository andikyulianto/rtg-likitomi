from django.shortcuts import render_to_response
from django.core.cache import cache
from datetime import datetime
import sys

import serial

from weight.models import TempWeight

# Setting scale mode = {'real', 'fake'}
	scale_mode = 'real'

def scale(request):
	"""
	Views of scale application.

		Connect and retrieve the weight from weighing indicator via serial port.

		Connect and retrieve the paper roll tag information from RFID reader.

		Update the temporary weight of a particular paper roll.

	**Context:**

	``Models``

		:model:`weight.TempWeight`

	``Special Modules``

		serial: For making a connection to weighing indicator.

	**Template:**

	:template:`templates/clamplift/scale.html`

	"""

# Connect to scale via serial port
	if scale_mode == 'real':
		try:
			ser = serial.Serial()
			ser.baudrate = 2400
			ser.bytesize = 7
			ser.parity = 'E'
			ser.stopbits = 1
			ser.timeout = 1
			if sys.platform == 'linux2': # on GNU/Linux
				for i in range(8):
					try:
						ser.port = '/dev/ttyUSB'+str(i)
						ser.open()
						ser.flushInput()
						output = ser.readline()
					except:
						serror = "Cannot use port USB"+str(i)
			if sys.platform == 'win32': # on Windows
				for i in range(8):
					try:
						ser.port = 'COM'+str(i)
						ser.open()
						ser.flushInput()
						output = ser.readline()
					except:
						serror = "Cannot use port COM"+str(i)
			ser.close()
		except serial.SerialException:
			serror = "Cannot connect to scale"

		if not serror:
			if output:
				a = output.rsplit(",")
				if len(a) == 3:
					if a[0] == 'ST':
						b = a[2]
						if b[0:1] == '+':
							weight = float(b.rsplit("+")[1].rsplit("kg")[0])
							# Store the weight to database
							if weight != TempWeight.objects.order_by('-timestamp')[0].weight:
								if TempWeight.objects.count() >= 10:
									p = TempWeight.objects.order_by('timestamp')[0]
									p.delete()
									TempWeight.objects.create(weight=weight)
								else:
									TempWeight.objects.create(weight=weight)
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
						serror = "Unstable weight data or Overload"
				else:
					serror = "Incomplete data"
			else:
				serror = "No data received"

	if scale_mode == 'fake': # Fake mode just for running application without weighing indicator
		output = "ST,GS,+00483.0kg\r\n"
		a = output.rsplit(",")
		if len(a) == 3:
			if a[0] == 'ST':
				b = a[2]
				if b[0:1] == '+':
					weight = float(b.rsplit("+")[1].rsplit("kg")[0])
					# Store the weight to database
					if weight != TempWeight.objects.order_by('-timestamp')[0].weight:
						if TempWeight.objects.count() >= 10:
							p = TempWeight.objects.order_by('timestamp')[0]
							p.delete()
							TempWeight.objects.create(weight=weight)
						else:
							TempWeight.objects.create(weight=weight)
				else:
					serror = "Negative value"
			else:
				serror = "Unstable weight data or Overload"
		else:
			serror = "Incomplete data"

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

	return render_to_response('scale.html', locals())

