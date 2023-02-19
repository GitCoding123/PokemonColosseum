# This class constructs Pokemon move data objects using getters and
# setters for name, type, category, contest, PP, power, and accuracy.
class MovesData:

    # __init__() function intializes our attributes for our objects
    def __init__(self, name, type, category, contest, PP, power, accuracy):
        self.name = name
        self.type = type
        self.category = category
        self.contest = contest
        self.PP = PP
        self.power = power
        self.accuracy = accuracy

    # returns name
    def get_name(self):
        return self.name
    # sets name
    def set_name(self, name):
        self.name = name

    # returns type
    def get_type(self):
        return self.type
    # sets type
    def set_type(self, type):
        self.type = type

    # returns category
    def get_category(self):
        return self.category
    # sets category
    def set_category(self, category):
        self.category = category

    # returns contest
    def get_contest(self):
        return self.contest
    # sets contest
    def set_contest(self, contest):
        self.contest = contest

    # returns PP
    def get_PP(self):
        return self.PP
    #sets PP
    def set_PP(self, PP):
        self.PP = PP

    # returns power
    def get_power(self):
        return self.power
    # sets power
    def set_power(self, power):
        self.power = power

    # returns accuracy
    def get_accuracy(self):
        return self.accuracy
    # sets accuracy
    def set_accuracy(self, accuracy):
        self.accuracy = accuracy