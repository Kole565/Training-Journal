class Training():

    def __init__(self, values):
        self.date = values["date"]
        self.time = values["time"]
        self.description = values["description"]

        self.type = "other"
    
    @staticmethod
    def fields():
        return ["date", "time", "description"]

    def values(self):
        return [self.date, self.time, self.description]
    
    def get_saving_stm(self, table):
        basis = self.request_to_insert(table)
        arguments_num = self.get_arguments_num()
        placeholders = self.placeholders_string(arguments_num)

        return "{0} {1}".format(basis, placeholders)
    
    def request_to_insert(self, table):
        basis = "INSERT INTO {0} ".format(table)
        basis += "VALUES"

        return basis
    
    def get_arguments_num(self):
        return len(self.values())
    
    def placeholders_string(self, num):
        assert num >= 1, "Placeholders amount should be more 0"

        placeholders = "({0}?)".format("?, " * (num-1))

        return placeholders
        