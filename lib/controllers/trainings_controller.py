import sqlite3
from lib.models.training import Training

class TrainingsController():
	
	"""Trainings collection.

	Handle, edit training objects.
	Operate with sqlite db.

	"""

	path_db = "./db"

	def __init__(self, db=""):
		"""Initialize controller
		
		Attributes:
		self.trainings - local collection of trainings

		"""
		self.trainings = []

		if db:
			self.open_connection(db)
			self.create_cursor()
	
	def count(self):
		"""Return local collection size."""
		return len(self.trainings)
	
	def create(self, **data):
		"""New training."""
		self.trainings.append(Training(**data))
	
	def delete(self, ind):
		"""Delete train by ind."""
		try:
			del self.trainings[ind]
		except IndexError:
			print("Train by ind {0} not founded.".format(ind))
	
	def all_local(self):
		"""Print controller collection."""
		ret = ""
		for i in range(len(self.trainings)):
			ret += self.show_local(i)
			
		return ret
	
	def show(self, ind):
		"""Print training by index.
		
		Arguments:
		ind -- training index in db

		"""
		pass
	
	def clear(self):
		"""Clear local storage."""
		self.trainings = []
	
	# 
	# DB operate
	# 
	
	def open_connection(self, name):
		"""Open db file with name."""
		try:
			self.current_connection = sqlite3.connect(
												"{0}/{1}".format(self.path_db, name))
		except Exception as e:
			print(e)
	
	def close_connection(self):
		"""Close db file."""
		self.current_connection.close()
	
	def create_cursor(self):
		"""Create cursor for db requests."""
		self.current_cursor = self.current_connection.cursor()
	
	def sql_execute(self, stm_data):
		"""Execute sqlite statement."""
		self.current_cursor.execute(stm_data[0], stm_data[1])
	
	def commit(self):
		"""Commit changes to db."""
		self.current_connection.commit()
	
	def save(self):
		"""Push local collection to db."""
		if self.count() == 0: return "Nothing to save."

		for item in self.trainings:
			self.sql_execute(item.get_save())
		self.commit()
		self.clear()
		
		return
