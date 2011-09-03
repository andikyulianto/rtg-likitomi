from django.shortcuts import render_to_response
from django.core.cache import cache
from datetime import datetime

import serial

from weight.models import TempWeight

# Setting scale mode = {'real', 'fake'}
scale_mode = 'real'

# Serial port setting
ser = serial.Serial()
ser.baudrate = 2400
ser.bytesize = 7
ser.parity = 'E'
ser.stopbits = 1
ser.timeout = 1
ser.port = 'COM4'

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
			ser.open()
			ser.flushInput()
			output = ser.readline()
			ser.close()
		except:
			weight = ""
			serror = "Cannot open port "+ser.portstr

		weight = 0.0

		if not serror:
			a = output.rsplit(",")
			if len(a) == 3:
				if a[0] == 'ST':
					b = a[2]
					if b[0:1] == '+':
						c = float(b.rsplit("+")[1].rsplit("kg")[0])
						cache.set('data', c, 5)
						# Store the weight to database
						if weight != TempWeight.objects.order_by('-timestamp')[0].weight:
							if TempWeight.objects.count() >= 10:
								p = TempWeight.objects.order_by('timestamp')[0]
								p.delete()
								TempWeight.objects.create(weight=weight)
							else:
								TempWeight.objects.create(weight=weight)
					else:
						serror = " (Negative value)"
				else:
					serror = " (Unstable or overload)"
			else:
				serror = " (Incomplete data)"

			weight = cache.get('data')

	if scale_mode == 'fake': # Fake mode just for running application without weighing indicator
		weight = 482.0
		# Store the weight to database
		if weight != TempWeight.objects.order_by('-timestamp')[0].weight:
			if TempWeight.objects.count() >= 10:
				p = TempWeight.objects.order_by('timestamp')[0]
				p.delete()
				TempWeight.objects.create(weight=weight)
			else:
				TempWeight.objects.create(weight=weight)

	return render_to_response('scale.html', locals())

