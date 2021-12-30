import os
import sys

PROJECT_ROOT = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(PROJECT_ROOT)

import unittest
from unittest.mock import patch, call

from lib.executor import Executor

from lib.trainings.training import Training
from scripts.add_train import *


class TestTrainAdder(unittest.TestCase):
    
    def setUp(self):
        self.adder = TrainAdder()

    @patch("builtins.print")
    def test_show_types(self, mock_print):
        expected = "Avaliable types for now:\n\tOther\n\tRun\n\n"
        
        self.adder.show_types()
        
        self.assertEqual(mock_print.mock_calls[0], call(expected))
    
    def test_types(self):
        self.assertEqual(self.adder.types(), ["other", "run"])
    
    @patch("builtins.input")
    def test_get_type_and_values(self, mock_input):
        mock_input.side_effect = ["other", "01.01.2000", "10:00", "test"]

        self.adder.get_type_and_values()

        self.assertEqual(self.adder.choosed_train.__name__, "Training")
        self.assertEqual(self.adder.values,
                 {"date": "01.01.2000", "time": "10:00", "description": "test"})
    
    def test_create(self):
        self.adder.choosed_train = self.adder.TYPES_TO_CLASSES["other"]
        self.adder.values = {
                   "date": "01.01.2000", "time": "10:00", "description": "test"}
        
        self.adder.create()

        self.assertEqual(self.adder.train.__class__.__name__, "Training")
    
    def test_save(self):
        self.adder.train = Training({
            "date": "01.01.2000", "time": "10:00", 
            "description": "test"
        })

        self.do_in_temp_db(self.adder.save)
        # TODO: Extract to helper "do_in_temp_db", other
    

    def do_in_temp_db(self, func, *args, **kwargs):
        self.init_executor()
        self.destroy_temp_db_if_exist()
        self.create_temp_db_if_need()

        func(*args, **kwargs)

        self.destroy_temp_db_if_exist()
    
    def init_executor(self):
        self.executor = Executor("temp")
    
    def destroy_temp_db_if_exist(self):
        if os.path.exists(self.executor.db_path()):
            os.remove(self.executor.db_path())
    
    def create_temp_db_if_need(self):
        if os.path.exists(self.executor.db_path()):
            return
            
        open(self.executor.db_path(), "w").close()

        self.executor.connect()
        self.executor.execute("""
            CREATE TABLE IF NOT EXISTS other (
                date text,
                time text,
                description text
                );
            """)
        self.executor.commit()
        self.executor.disconnect()
