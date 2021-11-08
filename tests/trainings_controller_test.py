import unittest

import os, sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(parent_dir)

from lib.controllers.trainings_controller import TrainingsController

class TestTrainingController(unittest.TestCase):

	def setUp(self):
		self.cont = TrainingsController()
		
		self.cont.create(time="30", distance=150)
		self.cont.create(time="10:00", distance=2000)
		self.cont.create(time="15:00", distance=2500)
		
	def test_count(self):		
		self.assertEqual(self.cont.count, 3)
	
	def test_all_local(self):
		compare_str = ""
		compare_str += "Time: 30 sec\nDistance: 150 m\n\n"
		compare_str += "Time: 10 min\nDistance: 2 km\n\n"
		compare_str += "Time: 15 min\nDistance: 2 km 500 m\n\n"

		self.assertEqual(self.cont.all_local(), compare_str)

		self.assertEqual(self.cont.show_local(0), 
		"Time: 30 sec\nDistance: 150 m\n\n"
		)
		self.assertEqual(self.cont.show_local(1), 
		"Time: 10 min\nDistance: 2 km\n\n"
		)
		self.assertEqual(self.cont.show_local(2), 
		"Time: 15 min\nDistance: 2 km 500 m\n\n"
		)

		
if __name__ == "__main__":
	unittest.main()