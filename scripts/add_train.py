import os
import sys

PROJECT_ROOT = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(PROJECT_ROOT)

from lib.record import Record
from lib.record_io import RecordIO

from lib.training import Training
from lib.trainings.run import Run


DB = ""
TYPES_TO_CLASSES = {
    "other": Training,
    "run": Run
}


def add_train_by_input():
    show_types(TYPES_TO_CLASSES.keys())
    print()
    
    train = get_type_and_create()

    save(train)

def show_types(types):
    print("Avaliable types for now:")
    for type in types:
        print("\t{0}".format(type.capitalize()))

def get_type_and_create():
    choosed_train = TYPES_TO_CLASSES[ask_and_get_type().lower()]
    values = ask_and_get_values(choosed_train.fields())
    train = choosed_train(values)

    return train

def ask_and_get_type():
    io = RecordIO()
    
    io.ask("type")
    io.get_and_save("type")

    return io.input_buffer["type"]

def ask_and_get_values(types):
    io = RecordIO()
    
    io.ask_save_multi(types)

    return io.input_buffer

def save(train):
    record = Record(DB, train.type, train)
    record.save()
    

if __name__ == "__main__":
    add_train_by_input()
