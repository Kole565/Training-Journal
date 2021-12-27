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
        print("Avaliable types for now:")
        for type in self.types():
            print("\t{0}".format(type.capitalize()))
        print()
    
    def types(self):
        return list(self.TYPES_TO_CLASSES.keys())
    
    def get_type_and_values(self):
        self.choosed_train = TYPES_TO_CLASSES[self.ask_and_get_type().lower()]
        self.values = self.ask_and_get_values(self.choosed_train.fields())
    
    def ask_and_get_type(self):        
        self.io.ask("type")
        self.io.get_and_save("type")

        return self.io.get_and_clear_buffer()["type"]
    
    def ask_and_get_values(self, types):
        self.io.ask_save_multi(types)

        return self.io.get_and_clear_buffer()
    
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
