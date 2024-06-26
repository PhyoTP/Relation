class Relator:
    def __init__(self, name, relations=None, children=None, parents=None):
        self.name = name
        self.relations = relations if relations is not None else []
        self.children = children if children is not None else []
        self.parents = parents if parents is not None else []
    
    def __mul__(self, other):
        if other not in self.relations:
            self.relations.append(other)
        if self not in other.relations:
            other.relations.append(self)
    
    def __add__(self, other):
        if other not in self.children:
            self.children.append(other)
        if self not in other.parents:
            other.parents.append(self)
    
    def __str__(self):
        return self.name
    
    def print_relations(self):
        print(f"{self.name}'s Relations:")
        for i in self.relations:
            print(i)
    
    def print_children(self):
        print(f"{self.name}'s Children:")
        for i in self.children:
            print(i)
    
    def print_parents(self):
        print(f"{self.name}'s Parents:")
        for i in self.parents:
            print(i)

def is_relator(cls):
    class_type = type(cls)
    if class_type is Relator:
        return True
    if Relator in class_type.__bases__:
        return True
    for base in class_type.__bases__:
        if type_is_relator(base):
            return True
    return False

def type_is_relator(class_type):
    if class_type is Relator:
        return True
    if Relator in class_type.__bases__:
        return True
    for base in class_type.__bases__:
        if type_is_relator(base):
            return True

# Testing
class Person(Relator):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
        self.calculate_followers()
    
    def calculate_followers(self):
        self.followers = len(self.children)
    
    def calculate_friends(self):
        for child in self.children:
            if self in child.children:
                self * child
                child * self
    
    def __add__(self, other):
        re = super().__add__(other)
        self.calculate_followers()
        other.calculate_followers()
        self.calculate_friends()
        other.calculate_friends()
        return re
    
    def __mul__(self, other):
        re = super().__mul__(other)
        return re

class Group(Relator):
    def __init__(self, name):
        super().__init__(name)
        self.calculate_members()
    
    def calculate_members(self):
        self.members = len(self.children)
    
    def __add__(self, other):
        re = super().__add__(other)
        self.calculate_members()
        return re

user = Person("Tim", 17)
friend = Person("Maddie", 16)
groupmate = Person("Jake", 23)
coding_club = Group("Coding Club")

user+friend
user.print_children()
friend+user
user.print_relations()
friend.print_relations()
coding_club+user
coding_club+groupmate
coding_club.print_children()
print(coding_club.members)