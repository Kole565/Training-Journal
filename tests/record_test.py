import os
import sys

PROJECT_ROOT = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(PROJECT_ROOT)

import unittest

from lib.record import Record
from lib.training import Training


class TestRecord(unittest.TestCase):

    root = os.path.join(os.path.dirname(__file__), "..")
    path_to_db_folder = root + "/db/"

    db_name = "temp"
    table = "others"


    def setUp(self):
        train = Training({
            "date": "01.01.2000", "time": "10:00", 
            "description": "test common training"
        })
        self.record = Record(self.db_name, self.table, train)
    
    def test_init(self):
        self.assertTrue(self.record)
    
    def test_init_attrs(self):
        self.assertEqual(self.record.db, self.db_name)
        self.assertEqual(self.record.table, self.table)
        self.assertTrue(self.record.record)
        
    def test_connection_and_cursor(self):
        self.record.open_connection()
        self.assertEqual(type(self.record.connection).__name__, "Connection")

        self.record.init_cursor()       
        self.assertEqual(type(self.record.cursor).__name__, "Cursor")

        self.record.close_connection_and_cursor()
    
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
            CREATE TABLE IF NOT EXISTS others (
                date text,
                time text,
                description text
                );
            """)
