import os, sys

PROJECT_ROOT = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(PROJECT_ROOT)

import unittest

from lib.record import Record
from lib.training import Training


class TestTraining(unittest.TestCase):

    root = os.path.join(os.path.dirname(__file__), "..")

    path_to_db_folder = root + "/db/"
    db_name = "temp"
    table = "trainings"


    def setUp(self):
        values = {
            "date": "01.01.2000", "time": "10:00", 
            "description": "test training"
        }

        self.training = Training(values)
        self.record = Record(self.db_name, self.table, self.training)

    def test_init(self):
        self.assertTrue(self.training)
        
    def test_values(self):
        self.assertEqual(len(self.training.values()), 3)
    
    def test_get_arguments_num(self):
        self.assertEqual(self.training.get_arguments_num(), 3)


# if __name__ == "__main__":
#     unittest.main()