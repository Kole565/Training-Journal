import unittest

import os, sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(parent_dir)

from lib.models.training import Training

class TestTraining(unittest.TestCase):

	def test_training_new_empty(self):
		"""
		Test how training will be created with zero args
		"""
		training = Training()
		self.assertIsNotNone(training)

	def test_training_short_new(self):
		"""
		Test how training will be created.
		Short values used
		"""
		training = Training(time="30", distance=150)

		self.assertEqual(training.time, "30")
		self.assertEqual(training.formated_time(), "30 sec")

		self.assertEqual(training.distance, 150)
		self.assertEqual(training.formated_distance(), "150 m")
	
	def test_training_short_new(self):
		"""
		Test how training will be created.
		Maraphon-like values used
		"""
		training = Training(time="4:02:30", distance=42200)

		self.assertEqual(training.time, "4:02:30")
		self.assertEqual(training.formated_time(), "4 h 2 min 30 sec")

		self.assertEqual(training.distance, 42200)
		self.assertEqual(training.formated_distance(), "42 km 200 m")


if __name__ == "__main__":
	unittest.main()