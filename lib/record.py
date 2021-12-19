import sqlite3
import os


class Record():

    root = os.path.join(os.path.dirname(__file__), "..")
    path_to_db_folder = root + "/db"
    db_format = ".db"

    def __init__(self, db, table, record):
        self.db = db
        self.table = table
        self.record = record
    
    def save(self):
        stm = self.record.get_save_stm(self.table)
        values = self.record.get_save_values()

        self.open_connection()
        self.init_cursor()
        self.execute_with_values(stm, values)
        self.commit()
        self.close_connection_and_cursor()

    def open_connection(self):
        self.connection = sqlite3.connect(self.db_path())
    
    def db_path(self):
        path = "{0}/{1}".format(self.path_to_db_folder, self.db)
        return path + self.db_format
    
    def init_cursor(self):
        self.cursor = self.connection.cursor()
        
    def execute_with_values(self, stm, values):
        print(stm)
        print(values)
        return self.cursor.execute(stm, values).fetchall()
    
    def execute(self, stm):
        return self.cursor.execute(stm).fetchall()
    
    def commit(self):
        self.connection.commit()
    
    def close_connection_and_cursor(self):
        self.connection.close()
        self.cursor = None
        