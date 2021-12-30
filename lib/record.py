import os
import sys

PROJECT_ROOT = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(PROJECT_ROOT)

from lib.executor import Executor


class Record():

    def __init__(self, db, record):
        self.executor = Executor(db)

        self.record = record
    
    def save(self):
        stm = self.record.get_saving_stm()
        values = self.record.values()

        self.executor.connect()
        self.executor.execute_with_values(stm, values)
        self.executor.commit()
        self.executor.disconnect()
