import os, sys

PROJECT_ROOT = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(PROJECT_ROOT)

from lib.training import Training


class Run(Training):

    def __init__(self, values):
        self.duration = values["duration"]
        self.distance = values["distance"]
        
        super().__init__(values)
        
        self.type = "run"
        
    def fields(self):
        return super().fields() + ["duration", "distance"]
    
    def values(self):
        return super().values() + [self.duration, self.distance]
    
    def get_save_stm(self, table):
        placeholders = len(self.values())
        stm = super().get_save_stm_by_placeholders_num(table, placeholders)
        return stm
