class RecordIO():
    
    """RecordIO class
    
    Ask user for training data.

    """

    def __init__(self):
        self.input_buffer = {}
    
    def clear(self):
        self.input_buffer = {}

    def ask_save_multi(self, names):
        for name in names:
            self.ask(name)
            self.get_and_save(name)

    def ask(self, name):
        print("Enter {0}:".format(name.capitalize()))
    
    def get_and_save(self, name):
        self.input_buffer[name.lower()] = input()
    
    def get_and_return(self):
        return input()
        