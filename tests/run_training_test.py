import os
import sys

PROJECT_ROOT = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(PROJECT_ROOT)

import unittest

from lib.record import Record
from lib.trainings.run import Run


class TestRunTraining(unittest.TestCase):

    path_to_db_folder = PROJECT_ROOT + "/db/"
    db_name = "temp"

    def setUp(self):
        values = {
            "date": "01.01.2000", "time": "10:00", 
            "description": "test run", "duration": "15:00", "distance": "2 km"
        }

        self.train = Run(values)
        self.record = Record(self.db_name, self.train)
        

    def test_init(self):
        self.assertTrue(self.train)
    
    def test_init_attrs(self):
        self.assertEqual(self.train.duration, "15:00")
        self.assertEqual(self.train.distance, "2 km")
    
    def test_type(self):
        self.assertEqual(self.train.type, "run")
        
    def test_values(self):
        self.assertEqual(len(self.train.values()), 5)
    
    def test_get_saving_stm(self):
        stm = "INSERT INTO {0} VALUES ".format(self.train.type)
        stm += "(?, ?, ?, ?, ?)"
        
        self.assertEqual(self.train.get_saving_stm(), stm)
