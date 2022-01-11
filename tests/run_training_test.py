import os
import sys

PROJECT_ROOT = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(PROJECT_ROOT)

import unittest

from lib.trainings.run import Run


class TestRunTraining(unittest.TestCase):

    def setUp(self):
        values = {
            "date": "01.01.2000", "time": "10:00", 
            "description": "test run", "duration": "15:00", "distance": "2 km"
        }

        self.train = Run(values)
        

    def test_init(self):
        self.assertTrue(self.train)
    
    def test_init_attrs(self):
        self.assertEqual(self.train.duration, "15:00")
        self.assertEqual(self.train.distance, "2 km")
    
    def test_type(self):
        self.assertEqual(self.train.type, "run")
        
    def test_values(self):
        self.assertEqual(len(self.train.values()), 5)
