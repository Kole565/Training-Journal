import os
import sys

PROJECT_ROOT = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(PROJECT_ROOT)

from lib.record import Record
from lib.record_io import RecordIO

from lib.training import Training
from lib.trainings.run import Run


DB = ""
types_to_classes = {
    "other": Training,
    "run": Run
}


if __name__ == "__main__":
    print("Avaliable train types for now:")
    for type in types_to_classes.keys():
        print("\t{0}".format(type.capitalize()))
    print()
    
    train_record = RecordIO()
    
    train_record.ask("type")
    train_record.get_and_save("type")
    new_train = types_to_classes[train_record.input_buffer["type"].lower()]
    
    train_record.clear()
    train_record.ask_save_multi(new_train.fields())
    values = train_record.input_buffer
    
    train = new_train(values)
    record = Record(DB, train.type, train)
    record.save()