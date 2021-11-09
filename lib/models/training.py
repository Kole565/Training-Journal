class Training():
	
	"""Training session

	Handle one training with properties. (watch __init__)

	"""
	
	def __init__(self, **data):
		# TODO: 
		# - add duration, date convert (to time_date types)
		# - add runs support
		# - add series
		"""Construct training object

		Attributes:
		:name     - custom train name
		:duration - how long did train last (1:20:30)
		:date     - when did the train take place
		:note     - what user think about this train

		"""
		self.name     = data.get("name")
		self.duration = data.get("duration")
		self.date     = data.get("date")
		self.note     = data.get("note")
	
	def get_save(self):
		"""Return sql statement, values, that save current training."""
		stm = """	INSERT INTO trainings(name,duration,date,note)
					VALUES(?,?,?,?)"""
		values = (
			getattr(self, "name", None),
			getattr(self, "duration", None),
			getattr(self, "date", None),
			getattr(self, "note", None),
		)
		
		return (stm, values)
