import os, sys

PROJECT_ROOT = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(PROJECT_ROOT)

import unittest

from lib.training import Training


class TestTraining(unittest.TestCase):

    root = os.path.join(os.path.dirname(__file__), "..")

    path_to_db_folder = root + "/db/"
    db_name = "temp"
    table = "others"


    def setUp(self):
        values = {
            "date": "01.01.2000", "time": "10:00", 
            "description": "test training"
        }

        self.training = Training(values)        

    def test_init(self):
        self.assertTrue(self.training)
    
    def test_init_attrs(self):
        self.assertEqual(self.training.date, "01.01.2000")
        self.assertEqual(self.training.time, "10:00")
        self.assertEqual(self.training.description, "test training")
    
    def test_type(self):
        self.assertEqual(self.training.type, "other")
        
    def test_values(self):
        self.assertEqual(len(self.training.values()), 3)
    
    def test_get_saving_stm(self):
        need = "INSERT INTO {0} VALUES (?, ?, ?)".format(self.table)
        got = self.training.get_saving_stm(self.table)
        
        self.assertEqual(need, got)
    
    def test_get_arguments_num(self):
        self.assertEqual(self.training.get_arguments_num(), 3)


# if __name__ == "__main__":
#     unittest.main()
