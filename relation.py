class Relator:
    def __init__(self, name, relations=None, children=None, parents=None):
        self.name = name
        self.relations = relations if relations is not None else []
        self.children = children if children is not None else []
        self.parents = parents if parents is not None else []
    def __mul__(self, other):
        self.relations.append(other)
        other.relations.append(self)
    def __add__(self, other):
        self.children.append(other)
        other.parents.append(self)
    def __str__(self):
        return self.name
    def print_relations(self):
        for i in self.relations:
            print(i)
    def print_children(self):
        for i in self.children:
            print(i)
    def print_parents(self):
        for i in self.parents:
            print(i)
    def relations_in(self,param):
        included = []
        for i in param:
            if i in self.relations:
                included.append(i)
        return included
    def children_in(self,param):
        included = []
        for i in param:
            if i in self.children:
                included.append(i)
        return included
    def parents_in(self,param):
        included = []
        for i in param:
            if i in self.parents:
                included.append(i)
        return included
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

#testing
class Person(Relator):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
        self.calculate_followers()
    
    def calculate_followers(self):
        self.followers = len(self.relations)
class Group(Relator):
    def __init__(self, name):
        super().__init__(name)
        self.calculate_members 
    def calculate_members(self):
        self.members = len(self.children)
user = Person("Tim",17)
friend = Person("Maddie",16)
groupmate = Person("Jake",23)
coding_club = Group("Coding Club")
user.print_parents()
user.print_relations()
coding_club+user
coding_club+groupmate
user*friend
user.print_parents()
user.print_relations()
coding_club.print_children()
print(user.relations_in(user.parents))
user.parents[0].print_children

