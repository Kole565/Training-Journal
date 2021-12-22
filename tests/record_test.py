import os, sys

PROJECT_ROOT = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(PROJECT_ROOT)

import unittest

from lib.record import Record
from lib.training import Training


class TestRecord(unittest.TestCase):

    root = os.path.join(os.path.dirname(__file__), "..")

    path_to_db_folder = root + "/db/"
    db_name = "temp"
    table = "trainings"


    def setUp(self):
        train = Training({
            "date": "01.01.2000", "time": "10:00", 
            "description": "test training"
        })
        self.record = Record(self.db_name, self.table, train)
    
    def destroy_temp_db_if_exist(self):
        if os.path.exists(self.record.db_path()):
            os.remove(self.record.db_path())
    
    def create_temp_db_if_need(self):
        if not os.path.exists(self.record.db_path()):
            open(self.record.db_path(), "w").close()

            self.record.open_connection()
            self.record.init_cursor()
            self.record.execute("""CREATE TABLE IF NOT EXISTS trainings (
                date text,
                time text,
                description text
                );""")
    
    def test_init(self):
        self.assertTrue(self.record)
        
    def test_connection(self):
        self.record.open_connection()
        self.record.close_connection_and_cursor()
    
    def test_save(self):
        self.destroy_temp_db_if_exist()
        self.create_temp_db_if_need()
        self.record.save()
        self.destroy_temp_db_if_exist()
        

# if __name__ == "__main__":
#     unittest.main()