class Relator:
    def __init__(self, name, relations=None, children=None, parents=None):
        self.name = name
        self.relations = relations if relations is not None else []
        self.children = children if children is not None else []
        self.parents = parents if parents is not None else []
    
    def __mul__(self, other):
        if other not in self.relations:
            self.relations.append(other)
        if isinstance(other, Relator) and self not in other.relations:
            other.relations.append(self)
    
    def __add__(self, other):
        if not isinstance(other,type([])):
            yes = [other]
        else:
            yes = other
        for i in yes:
            if i not in self.children:
                self.children.append(i)
            if isinstance(i, Relator) and self not in i.parents:
                i.parents.append(self)
    def __radd__(self, other):
        if not isinstance(other,type([])):
            yes = [other]
        else:
            yes = other
        for i in yes:
            if i not in self.parents:
                self.parents.append(i)
            if isinstance(i, Relator) and self not in i.children:
                i.children.append(self)

    def __ior__(self, other):
        self.children += other.children
        self.relations += other.relations
        self.parents += other.parents
        return self
    
    def __or__(self, other):
        self.children += other.children
        self.relations += other.relations
        self.parents += other.parents
        other.children += self.children
        other.relations += self.relations
        other.parents += self.parents

        
    def __str__(self):
        return self.name
    
    def relations_names(self):
        return [str(i) for i in self.relations]
    
    def children_names(self):
        return [str(i) for i in self.children]
    
    def parents_names(self):
        return [str(i) for i in self.parents]
    def relation_is_type_names(self, type):
        return [str(i) for i in self.relations if isinstance(i,type)]
    def children_is_type_names(self, type):
        return [str(i) for i in self.children if isinstance(i,type)]
    def parents_is_type_names(self, type):
        return [str(i) for i in self.parents if isinstance(i,type)]
    def relation_is_type(self, type):
        return [i for i in self.relations if isinstance(i,type)]
    def children_is_type(self, type):
        return [i for i in self.children if isinstance(i,type)]
    def parents_is_type(self, type):
        return [i for i in self.parents if isinstance(i,type)]
        
# deprecated, use issubclass(obj, Relator) instead

# def is_relator(cls):
#     class_type = type(cls)
#     if class_type is Relator:
#         return True
#     if Relator in class_type.__bases__:
#         return True
#     for base in class_type.__bases__:
#         if type_is_relator(base):
#             return True
#     return False

# def type_is_relator(class_type):
#     if class_type is Relator:
#         return True
#     if Relator in class_type.__bases__:
#         return True
#     for base in class_type.__bases__:
#         if type_is_relator(base):
#             return True
