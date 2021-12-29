import os
import sys

PROJECT_ROOT = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(PROJECT_ROOT)

import unittest
from unittest.mock import patch, call

from lib.record_io import RecordIO


class TestRecordIO(unittest.TestCase):
    
    def setUp(self):
        self.record_io = RecordIO()

    def test_buffer_is_empty(self):
        self.assertEqual(self.record_io.input_buffer, {})
    
    def test_clear_buffer(self):
        self.record_io.input_buffer = {"test": "test"}

        self.record_io.clear()

        self.test_buffer_is_empty()
    
    @patch("builtins.print")
    @patch("builtins.input")
    def test_ask_save_multi(self, mock_input, mock_print):
        mock_input.side_effect = ["first", "second"]
        
        self.record_io.ask_save_multi(["first", "second"])
        
        self.assertEqual(self.record_io.input_buffer, 
                                         {"first": "first", "second": "second"})
        self.assertEqual(mock_print.mock_calls,
                                  [call("Enter First:"), call("Enter Second:")])
    
    @patch("builtins.print")
    def test_ask(self, mock_print):
        self.record_io.ask("name")

        self.assertEqual(mock_print.mock_calls[0], call("Enter Name:"))
    
    @patch("builtins.input", return_value="name")
    def test_get_and_save(self, mock_input):
        self.record_io.get_and_save("test")

        self.assertEqual(self.record_io.input_buffer["test"], "name")
    
    @patch("builtins.input", return_value="name")
    def test_get_and_return(self, mock_input):
        ret = self.record_io.get_and_return()

        self.assertEqual(ret, "name")

