import os
import sys

PROJECT_ROOT = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(PROJECT_ROOT)

from lib.record import Record


DB = ""
TABLES = [
    "other",
    "run"
]


def select_all():
    executor = Record(DB, None, None)

    executor.open_connection()
    executor.init_cursor()
    
    columns = []
    values = []
    
    for table in TABLES:
        table_response = select_table(executor, table)
        
        columns.append(table_response[0])
        values.append(table_response[1])
        
    executor.close_connection_and_cursor()
    
    return columns, values

def select_table(executor, table):
    columns = []
    values = []
    
    select_columns = "PRAGMA table_info({0});".format(table)
    select_values = "SELECT * FROM {0};".format(table)

    columns += executor.execute(select_columns)
    values += executor.execute(select_values)

    return columns, values

def show_pretty(columns, values):
    for table in range(len(columns)):
        show_pretty_table(columns[table], values[table])

def show_pretty_table(columns, values):
    for record in range(len(values)):
        show_pretty_record(columns, values, record)

def show_pretty_record(columns, values, record):
    print("{0} {1}:".format(values[record][0], values[record][1]))
    print("\t{0}".format(values[record][2]))
    
    for n in range(3, len(values[record])):
        print("\t{0}: {1}".format(columns[n][1].capitalize(), values[record][n]))
        
    print()
        

if __name__ == "__main__":
    all = select_all()
    
    show_pretty(*all)
    