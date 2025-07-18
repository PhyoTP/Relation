from relation import Relator
from map import create_graph
topics = {}

class Topic(Relator):
    @classmethod
    def get(cls, name, relations=None, children=None, parents=None):
        if name in topics:
            existing = topics[name]
            existing |= Relator(name, relations, children, parents)
            return existing
        else:
            instance = cls(name, relations, children, parents)
            topics[name] = instance
            return instance
        
    
class Description(Relator):
    pass

bioMolecules = Topic.get("Biological Molecules") 
bioMolecules * Description("Types", children=[Topic.get("Proteins"), Topic.get("Nucleic Acids"), Topic.get("Carbohydrates"), Topic.get("Lipids")])
Topic.get("Proteins") * Description("made of", children=[Topic.get("Polypeptides")])
Topic.get("Polypeptides") * Description("made of", children=[Topic.get("Amino Acids")])
Topic.get("Polypeptides") * Description("linked by", children=[Topic.get("Peptide Bonds")])

g = create_graph(bioMolecules)  # Create and visualize the graph
g.render('bionotes_graph', format='png', view=True)
print()





