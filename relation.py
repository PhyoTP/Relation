class Relator:
    def __init__(self, relations=None, children=None):
        self.relations = relations if relations is not None else []
        self.children = children if children is not None else []

    def __mul__(self, other):
        self.relations.append(other)
        other.relations.append(self)
class Atom(Relator):
    def __init__(self, name):
        self.name = name
class Metal(Atom):
    def __init__(self, electrons):
        self.electrons = electrons
test = Metal(electrons=0)
print(type(test))
print(type(test).__bases__[0].__bases__[0])

