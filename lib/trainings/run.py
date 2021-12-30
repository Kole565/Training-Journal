import os
import sys

PROJECT_ROOT = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(PROJECT_ROOT)

from lib.trainings.training import Training


class Run(Training):

    def __init__(self, values):
        self.duration = values["duration"]
        self.distance = values["distance"]
        
        super().__init__(values)
        
        self.type = "run"
    
    @staticmethod
    def fields():
        return Training.fields() + ["duration", "distance"]
    
    def values(self):
        return super().values() + [self.duration, self.distance]
    
    def get_saving_stm(self):
        basis = self.get_request_to_insert()
        arguments_num = self.get_arguments_num()
        placeholders = self.get_placeholders_string(arguments_num)

        return "{0} {1}".format(basis, placeholders)
