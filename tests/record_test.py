import os
import sys

PROJECT_ROOT = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(PROJECT_ROOT)

import unittest

from lib.record import Record
from lib.trainings.training import Training


class TestRecord(unittest.TestCase):

    def setUp(self):
        train = Training({
            "date": "01.01.2000", "time": "10:00", 
            "description": "test common training"
        })
        self.record = Record("temp", train)
    
    def test_init(self):
        self.assertTrue(self.record)
    
    def test_init_attrs(self):
        self.assertEqual(self.record.executor.__class__.__name__, "Executor")
        self.assertTrue(self.record.record)
    
    def test_save(self):
        self.do_in_temp_db(self.record.save)
    
    def do_in_temp_db(self, func, *args, **kwargs):
        self.destroy_temp_db_if_exist()
        self.create_temp_db_if_need()

        func(*args, **kwargs)

        self.destroy_temp_db_if_exist()
    
    def destroy_temp_db_if_exist(self):
        if os.path.exists(self.record.executor.db_path()):
            os.remove(self.record.executor.db_path())
    
    def create_temp_db_if_need(self):
        if os.path.exists(self.record.executor.db_path()):
            return
            
        open(self.record.executor.db_path(), "w").close()

        self.record.executor.connect()
        self.record.executor.execute("""
            CREATE TABLE IF NOT EXISTS other (
                date text,
                time text,
                description text
                );
            """)
        self.record.executor.commit()
        self.record.executor.disconnect()
