class Relator:
    def __init__(self, name, relations=None, children=None):
        self.name = name
        self.relations = relations if relations is not None else []
        self.children = children if children is not None else []

    def __mul__(self, other):
        self.relations.append(other)
        other.relations.append(self)
    def __add__(self, other):
        self.children.append(other)
    def __str__(self):
        return self.name
    def print_relations(self):
        print(self.name+"'s Relations:")
        for i in self.relations:
            print(i.name)
    def print_children(self):
        print(self.name+"'s Children:")
        for i in self.children:
            print(i.name)
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
class Atom(Relator):
    def boom():
        print("explosion")
class Metal(Atom):
    def drop():
        print("sound.play")
sodium = Metal("sodium")
oxygen = Atom("oxygen")

sodium*oxygen
oxygen+sodium
sodium.print_relations()
oxygen.print_children()
sodium.relations[0].name="cheese"
print(oxygen.name)
