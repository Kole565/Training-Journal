import os
import sys

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
    
    def test_init_attrs(self):
        self.assertEqual(self.training.duration, "15:00")
        self.assertEqual(self.training.distance, "2 km")
    
    def test_type(self):
        self.assertEqual(self.training.type, "run")
        
    def test_values(self):
        self.assertEqual(len(self.training.values()), 5)
    
    def test_get_saving_stm(self):
        stm = "INSERT INTO {0} VALUES ".format(self.table)
        stm += "(?, ?, ?, ?, ?)"
        
        self.assertEqual(self.training.get_saving_stm(self.table), stm)

    def test_save(self):
        self.do_in_temp_db(self.record.save)
    
    def do_in_temp_db(self, func, *args, **kwargs):
        self.destroy_temp_db_if_exist()
        self.create_temp_db_if_need()

        func(*args, **kwargs)

        self.destroy_temp_db_if_exist()
    
    def destroy_temp_db_if_exist(self):
        if os.path.exists(self.record.db_path()):
            os.remove(self.record.db_path())
    
    def create_temp_db_if_need(self):
        if os.path.exists(self.record.db_path()):
            return
            
        open(self.record.db_path(), "w").close()

        self.record.open_connection()
        self.record.init_cursor()
        self.record.execute("""
            CREATE TABLE IF NOT EXISTS runs (
                date text,
                time text,
                description text,
                duration text,
                distance text
                );
            """)

# if __name__ == "__main__":
#     unittest.main()
