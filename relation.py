class Relator:
    def __init__(self, name, relations=None, children=None, parents=None):
        self.name = name
        self.relations = relations if relations is not None else []
        self.children = children if children is not None else []
        self.parents = parents if parents is not None else []
        self.relations_count = len(self.relations)
        self.children_count = len(self.children)
        self.parents_count = len(self.parents)
    
    def __mul__(self, other):
        if other not in self.relations:
            self.relations.append(other)
            self.relations_count += 1
        if self not in other.relations:
            other.relations.append(self)
            other.relations_count += 1
    
    def __add__(self, other):
        if other not in self.children:
            self.children.append(other)
            self.children_count += 1
        if self not in other.parents:
            other.parents.append(self)
            other.parents_count += 1
    
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

class Group(Relator):
    def __init__(self, name, desc):
        super().__init__(name)
        self.desc = desc
user = Person("Tim", 17)
friend = Person("Maddie", 16)
groupmate = Person("Jake", 23)
coding_club = Group("Coding Club","a club for coding")

user + friend
user.print_children()
print("a")
friend + user
user.print_relations()
friend.print_relations()
print(user.children_count)
print(user.relations_count)
coding_club + user
coding_club + groupmate
coding_club.print_children()
print(coding_club.children_count)