import os
import sys

PROJECT_ROOT = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(PROJECT_ROOT)

from lib.record import Record
from lib.record_io import RecordIO

from lib.training import Training
from lib.trainings.run import Run

types_to_classes = {
    "other": Training,
    "run": Run
}

DB = ""


if __name__ == "__main__":
    inp_buffer = RecordIO()
    
    inp_buffer.ask("type")
    inp_buffer.get_and_save("type")
    train_init_class = types_to_classes[inp_buffer.input_buffer["type"]]
    
    inp_buffer.clear()
    inp_buffer.ask_save_multi(train_init_class.fields())
    values = inp_buffer.input_buffer
    
    train = train_init_class(values)
    record = Record(DB, train.type, train)
    record.save()