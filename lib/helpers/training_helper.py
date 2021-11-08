"""Helper for training journal app.

Handle generally used methods.

"""

def time_format(time):
	"""Convert time from xx:xx to seconds."""
	ret = 0 # Seconds
	
	pos = 0
	for time in reversed(time.split(":")):
		ret += int(time) * (60 ** pos)
		pos += 1
	
	return ret
		

def calc_pace(time, distance):
	"""Get time in format xx:xx:xx, distance in kilometers
	
	Return pace in min/km
	"""
	calc = time_format(time) / distance

	seconds = int(calc % 60)
	minuts = int(calc // 60)

	if len(str(seconds)) == 1:
		seconds = "0{0}".format(seconds)
	elif len(str(seconds)) == 0:
		seconds = "00"
	
	if len(str(minuts)) == 1:
		minuts = "0{0}".format(minuts)
	elif len(str(minuts)) == 0:
		minuts = "00"
		
	return "{0}:{1}".format(minuts, seconds)
