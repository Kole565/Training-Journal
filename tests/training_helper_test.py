import unittest

import os, sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(parent_dir)

from lib.helpers.training_helper import calc_pace

class TestTrainingMethods(unittest.TestCase):

	def test_calc_pace_simple(self):
		self.assertEqual(calc_pace("01:00", 2), "00:30")
		self.assertEqual(calc_pace("01:00", 1), "01:00")
		self.assertEqual(calc_pace("01:00", 0.125), "08:00")
	
	def test_calc_pace_advance(self):
		self.assertEqual(calc_pace("10:00", 1), "10:00")
		self.assertEqual(calc_pace("10:00", 2), "05:00")
		self.assertEqual(calc_pace("10:00", 4), "02:30")
		self.assertEqual(calc_pace("10:00", 4.5), "02:13")
	
	def test_calc_pace_limits(self):
		self.assertEqual(calc_pace("00:06", 1), "00:06")
		self.assertEqual(calc_pace("99:50", 1), "99:50")

if __name__ == "__main__":
	unittest.main()