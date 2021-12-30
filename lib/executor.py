import os
import sqlite3


class Executor():
    # TODO:
    #   Create tests for this class
    
    root = os.path.join(os.path.dirname(__file__), "..")
    db_folder = root + "/db"
    db_format = "db"

    def __init__(self, db):
        self.db = db
    
    def connect(self):
        self.connection = sqlite3.connect(self.db_path())
        self.cursor = self.connection.cursor()
    
    def disconnect(self):
        self.connection.close()
        self.cursor = None
    
    def db_path(self):
        return "{0}/{1}.{2}".format(self.db_folder, self.db, self.db_format)
    
    def execute(self, stm):
        return self.cursor.execute(stm).fetchall()
    
    def execute_with_values(self, stm, values):
        return self.cursor.execute(stm, values).fetchall()
    
    def commit(self):
        self.connection.commit()