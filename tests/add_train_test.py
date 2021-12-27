import os
import sys

PROJECT_ROOT = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(PROJECT_ROOT)

import unittest
from unittest.mock import patch, call
from io import StringIO

from scripts.add_train import *

class TestTrainAdder(unittest.TestCase):
    
    def setUp(self):
        self.adder = TrainAdder()

    @patch("sys.stdout", new_callable=StringIO)
    def test_show_types(self, mock_stdout):
        expected = "Avaliable types for now:\n\tOther\n\tRun\n\n"
        
        self.adder.show_types()
        
        self.assertEqual(mock_stdout.getvalue(), expected)
    
    def test_types(self):
        self.assertEqual(self.adder.types(), ["other", "run"])
