class Training():

    def __init__(self, values):
        self.date = values["date"]
        self.time = values["time"]
        self.description = values["description"]

        self.type = "other"
    
    def fields(self):
        return ["date", "time", "description"]

    def values(self):
        return [self.date, self.time, self.description]
    
    def get_save_stm(self, table):
        basis = self.get_stm_basis(table)
        placeholders = self.format_placeholders_by_num(len(self.values()))

        return "{0} {1}".format(basis, placeholders)
    
    def get_save_stm_by_placeholders_num(self, table, num):
        basis = self.get_stm_basis(table)
        placeholders = self.format_placeholders_by_num(num)

        return "{0} {1}".format(basis, placeholders)
    
    def get_stm_basis(self, table):
        basis = "INSERT INTO {0} ".format(table)
        basis += "VALUES"

        return basis
    
    def format_placeholders_by_num(self, num):
        placeholders = "({0}?)".format("?, " * (num-1))

        return placeholders
    
    def placeholders_num(self):
        return len(self.values())

    def get_save_values(self):
        return tuple(self.values())
        