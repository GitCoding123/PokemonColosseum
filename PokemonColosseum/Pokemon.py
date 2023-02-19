# This class constructs Pokemon objects using getters and
# setters for name, type, HP, attack, defense, height, weight,
# and moves.
class Pokemon:

    # __init__() function intializes our attributes for our objects
    def __init__(self, name, type, HP, attack, defense, height, weight, moves):
        self.name = name
        self.type = type
        self.HP = HP
        self.attack = attack
        self.defense = defense
        self.height = height
        self.weight = weight
        self.moves = moves

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
        
    # returns HP
    def get_HP(self):
        return self.HP
    # sets HP
    def set_HP(self, HP):
        self.HP = HP
        
    # returns attack
    def get_attack(self):
        return self.attack
    # sets attack
    def set_attack(self, attack):
        self.attack = attack

    # returns defense
    def get_defense(self):
        return self.defense
    # sets defense
    def set_defense(self, defense):
        self.defense = defense

    # returns height
    def get_height(self):
        return self.height
    # sets height
    def set_height(self, height):
        self.height = height

    #returns weight
    def get_weight(self):
        return self.weight
    # sets weight
    def set_weight(self, weight):
        self.weight = weight
        
    # return moves
    def get_moves(self):
        return self.moves
    # set moves
    def set_moves(self, moves):
        self.moves = moves
