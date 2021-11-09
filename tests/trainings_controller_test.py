import unittest

import os, sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(parent_dir)

from lib.controllers.trainings_controller import TrainingsController

class TestTrainingController(unittest.TestCase):
		
	def test_count(self):
		"""Test collection size counter."""
		cont = TrainingsController()
		
		self.assertEqual(cont.count(), 0)
		cont.create(name="Collection Size", duration="10:00")
		self.assertEqual(cont.count(), 1)
		cont.delete(0)
		self.assertEqual(cont.count(), 0)
	
	def test_save(self):
		"""Test push local strorage feature."""
		cont = TrainingsController("testDB.db")
		self.assertEqual(cont.save(), "Nothing to save.")
		
		train = cont.create(name="Test DB Train", duration="42:00")
		self.assertEqual(cont.count(), 1)
		self.assertFalse(cont.save())     # Controller return 0 if success
		self.assertEqual(cont.count(), 0)

		cont.close_connection() # Connection start automaticly, but close - not
		
		
if __name__ == "__main__":
	unittest.main()