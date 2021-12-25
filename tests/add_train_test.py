import os
import sys

PROJECT_ROOT = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(PROJECT_ROOT)

import unittest
from io import StringIO

from scripts.add_train import *

class TestAddTrain(unittest.TestCase):
    
    def setUp(self):
        self.capturedOut = StringIO()
        sys.stdout = self.capturedOut
    
    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_types_show(self):
        expected = "Avaliable types for now:\n\tFirst\n\tSecond\n\tThird\n"

        show_types(["first", "second", "third"])

        self.assertEqual(expected, self.capturedOut.getvalue())