class Training():
	
	"""Training session

	"""
	
	def __init__(self, **data):
		self.time = data.get("time")
		self.distance = data.get("distance")		
	
	def formated_time(self):
		time_list = reversed(list(map(int, self.time.split(":"))))
		time_form = {
			0: "sec",
			1: "min",
			2: "h"
		}

		ret = ""
		i = 0
		for time_item in time_list:
			if time_item != 0:
				ret = "{0} {1} ".format(time_item, time_form[i]) + ret
			i += 1
		
		return ret.strip()
	
	def formated_distance(self):
		ret = ""

		if self.distance < 1000:
			ret += "{0} m".format(self.distance)
		elif self.distance % 1000 == 0:
			ret += "{0} km".format(self.distance // 1000)			
		else:	
			ret += "{0} km {1} m".format(self.distance // 1000,
														self.distance % 1000)
		
		return ret


