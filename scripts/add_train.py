import shelve

import os
import sys


PROJECT_ROOT = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(PROJECT_ROOT)

from lib.trainings.training import Training

DB_FOLDER = os.path.join(PROJECT_ROOT, "db")


values = {
    "date": "01.01.20", "time": "10:00", 
    "description": "test training"
}

train = Training(values)
id = str(len(shelve.open(DB_FOLDER + "\db")))

with shelve.open(DB_FOLDER + "\db") as db:
    db[id] = train

    # print("All: ")
    # for key in db:
    #     print(key, " - ", str(db[key]))
