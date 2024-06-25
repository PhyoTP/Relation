class Relator:
    def __init__(self, relations=None, children=None):
        self.relations = relations if relations is not None else []
        self.children = children if children is not None else []

    def __mul__(self, other):
        self.relations.append(other)
        other.relations.append(self)
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
    def __init__(self, name):
        self.name = name
class Metal(Atom):
    def __init__(self, electrons):
        self.electrons = electrons
test = Metal(electrons=0)
print(is_relator(test))
print(type_is_relator(type(test)))
