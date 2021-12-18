import os, sys

PROJECT_ROOT = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(PROJECT_ROOT)

import unittest

from lib.record import Record
from lib.trainings.run import Run


class TestRunTraining(unittest.TestCase):

    root = os.path.join(os.path.dirname(__file__), "..")

    path_to_db_folder = root + "/db/"
    db_name = "temp"
    table = "runs"

    def setUp(self):
        values = {
            "date": "01.01.2000", "time": "10:00", 
            "description": "test run", "duration": "15:00", "distance": "2 km"
        }

        self.training = Run(values)
        self.record = Record(self.db_name, self.table, self.training)
        

    def test_init(self):
        self.assertTrue(self.training)
    
    def test_type(self):
        self.assertEqual(self.training.type, "run")
    
    def test_fields(self):
        self.assertEqual(len(self.training.fields()), 5)
        
    def test_values(self):
        self.assertEqual(len(self.training.values()), 5)
    
    def test_get_save_stm(self):
        stm = "INSERT INTO {0} VALUES ".format(self.table)
        stm += "(?, ?, ?, ?, ?)"
        
        self.assertEqual(self.training.get_save_stm(self.table), stm)


# if __name__ == "__main__":
#     unittest.main()