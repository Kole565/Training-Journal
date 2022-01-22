import shelve
import os
import sys

PROJECT_ROOT = os.path.join(os.path.dirname(__file__), "..")
DB_FOLDER = os.path.join(PROJECT_ROOT, "db")

sys.path.append(PROJECT_ROOT)

from lib.trainings.training import Training


asks = ["Enter date: ", "Enter time: ", "Describe train: (enter nothing for done)"]
fields = ["date", "time", "description"]

values = {}
for i in range(len(asks)):
    total_inp = ""
    while True:
        inp = input(asks[i])
        total_inp += inp + "\n"
        if not inp or fields[i] != "description":
            break
    
    values[fields[i]] = total_inp

train = Training(values)

with shelve.open(DB_FOLDER + "\db") as db:
    id = str(len(db))
    db[id] = train

    print("All: ")
    for key in db:
        print(key, " - ", str(db[key]))
