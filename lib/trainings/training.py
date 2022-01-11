from datetime import datetime


class Training():

    def __init__(self, values):
        self.date = datetime.strptime(values["date"], "%d.%m.%Y") 
        self.time = datetime.strptime(values["time"], "%M:%S").time()
        self.description = values["description"]

        self.type = "other"
    
    def __str__(self):
        ret = ""
        for value in self.values():
            ret += "{0}\n".format(str(value))
        
        return ret
    
    @staticmethod
    def fields():
        return ["date", "time", "description"]

    def values(self):
        return [self.date, self.time, self.description]
    
    def get_saving_stm(self):
        basis = self.get_request_to_insert()
        arguments_num = self.get_arguments_num()
        placeholders = self.get_placeholders_string(arguments_num)

        return "{0} {1}".format(basis, placeholders)
    
    def get_request_to_insert(self):

        basis = "INSERT INTO {0} ".format(self.type)
        basis += "VALUES"

        return basis
    
    def get_arguments_num(self):
        return len(self.values())
    
    def get_placeholders_string(self, num):
        assert num > 0, "Placeholders amount should be more 0"

        placeholders = "({0}?)".format("?, " * (num-1))

        return placeholders
        