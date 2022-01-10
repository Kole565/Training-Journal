import os
import sys

PROJECT_ROOT = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(PROJECT_ROOT)

import unittest

from lib.trainings.training import Training


class TestTraining(unittest.TestCase):
    
    def setUp(self):
        values = {
            "date": "01.01.2000", "time": "10:00", 
            "description": "test training"
        }

        self.train = Training(values)

    def test_init(self):
        self.assertTrue(self.train)
    
    def test_init_attrs(self):
        self.assertEqual(self.train.date, "01.01.2000")
        self.assertEqual(self.train.time, "10:00")
        self.assertEqual(self.train.description, "test training")
    
    def test_type(self):
        self.assertEqual(self.train.type, "other")
        
    def test_values(self):
        self.assertEqual(len(self.train.values()), 3)
