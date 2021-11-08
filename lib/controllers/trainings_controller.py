import sqlite3
from lib.models.training import Training

class TrainingsController():
	
	"""Trainings collection.

	Handle, edit training objects.
	Operate with sqlite db.

	"""

	def __init__(self, db=""):
		self.trainings = []
		self.count = 0

		if db:
			self.open_connection(db)
			self.create_cursor()
	
	def create(self, **data):
		"""New training."""
		self.trainings.append(Training(**data))
		self.count += 1
	
	def all_local(self):
		"""Print controller collection."""
		ret = ""
		for i in range(len(self.trainings)):
			ret += self.show_local(i)
			
		return ret
	
	def show_local(self, ind):
		"""Print training by index.
		
		Arguments:
		ind -- training index in collection

		"""
		ret = ""
		
		ret += "Time: {0}\n".format(self.trainings[ind].formated_time())
		ret += "Distance: {0}\n\n".format(self.trainings[ind].formated_distance())

		return ret
	
	def open_connection(self, name):
		rel_path = "./db"
		self.current_connection = sqlite3.connect(
											"{0}/{1}".format(rel_path, name))
	
	def close_connection(self):
		self.current_connection.close()
	
	def create_cursor(self):
		self.current_cursor = self.current_connection.cursor()
	
	def sql_execute(self, stm):
		self.current_cursor.execute(stm)
	
	def create_table(self, name, colomns):
		"""Create table from attrs

		Arguments:		
		name -- table name
		colomns -- [
			{
				"name": "colomn_name",
				"type": "colomn_data_type",

				"key": "is key?",
				"null": "is null?",
				"uniq": "is uniq?",
			},
		]

		"""
		stm = "CREATE TABLE [IF NOT EXISTS] "
		stm += "{0} ".format(name)
		stm += "(\n\t"
		for colomn in colomns:
			stm += "{0} ".format(colomn["name"])
			stm += "{0} ".format(colomn["type"])

			if colomn["key"]:		stm += "KEY "
			if not colomn["null"]:	stm += "NOT NULL "
			if colomn["uniq"]:		stm += "UNIQUE "

			stm += ",\n"

		stm += ");"

		self.sql_execute(stm)