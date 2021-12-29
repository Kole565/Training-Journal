import os
import sys

PROJECT_ROOT = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(PROJECT_ROOT)

from lib.record import Record
from lib.record_io import RecordIO

from lib.training import Training
from lib.trainings.run import Run


class TrainAdder():

    DB = ""
    TYPES_TO_CLASSES = {
        "other": Training,
        "run": Run
    }

    def __init__(self):
        self.io = RecordIO()
        self.train = None

    def show_types(self):
        msg = "Avaliable types for now:\n"
        for type in self.types():
            msg += "\t{0}\n".format(type.capitalize())
        msg += "\n"
        
        print(msg)
    
    def types(self):
        return list(self.TYPES_TO_CLASSES.keys())
    
    def get_type_and_values(self):
        self.choosed_train = self.TYPES_TO_CLASSES[
                                                self.ask_and_get_type().lower()]
        self.values = self.ask_and_get_values(self.choosed_train.fields())
    
    def ask_and_get_type(self):        
        self.io.ask("type")

        return self.io.get_and_return()
    
    def ask_and_get_values(self, types):
        self.io.ask_save_multi(types)
        buffer = self.io.input_buffer
        self.io.clear()
        
        return buffer
    
    def create(self):
        self.train = self.choosed_train(self.values)
        
    def save(self):
        record = Record(self.DB, self.train.type, self.train)
        record.save()


if __name__ == "__main__":
    adder = TrainAdder()

    adder.show_types()
    adder.get_type_and_values()
    adder.create()
    adder.save()

    input()
