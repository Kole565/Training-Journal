import unittest, datetime

import os, sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(parent_dir)

from lib.models.training import Training

class TestTraining(unittest.TestCase):

	def test_training_new_empty(self):
		"""Test zero args training object creating."""
		training = Training()
		self.assertIsNotNone(training)

	def test_training_short_new(self):
		"""Test short training object creating."""
		training = Training(name="Short Train")

		self.assertEqual(training.name,     "Short Train")
		self.assertEqual(training.duration, None)
		self.assertEqual(training.date,     None)
		self.assertEqual(training.note,     None)
	
	def test_training_long_new(self):
		"""Test long training object creating."""
		training = Training(name="Long Train", duration="4:02:30", 
							date="01.01.2000", note="This train is loong!")

		self.assertEqual(training.name,           "Long Train")
		self.assertEqual(type(training.duration), datetime.time)
		self.assertEqual(type(training.date),     datetime.date)
		self.assertEqual(training.note,           "This train is loong!")


if __name__ == "__main__":
	unittest.main()
