from relation import Relator
from relation.map import create_graph
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

def convert_topic(str):
    sentences = str.splitlines()
    for sentence in sentences:
        parts = sentence.split(",")
        if len(parts) == 2:
            Topic.get(parts[0].strip()) * Description(parts[1].strip())
        elif len(parts) > 2:
            Topic.get(parts[0].strip()) * Description(parts[1].strip(), children=[Topic.get(part.strip()) for part in parts[2:]])
        

bioMolecules = Topic.get("Biological Molecules") 
convert_topic("""
Biological Molecules, types, Proteins, Nucleic Acids, Carbohydrates, Lipids
Proteins, made of, Polypeptides
Polypeptides, made of, Amino Acids
Amino Acids, link together by, Peptide Bonds
Carbohydrates, types, Monosaccharides, Disaccharides, Polysaccharides
Monosaccharides, examples, Glucose, Fructose, Galactose
Disaccharides, examples, Sucrose, Lactose, Maltose
Polysaccharides, examples, Starch, Glycogen, Cellulose
Monosaccharides, link together by, Glycosidic Bonds
Disaccharides, made of, Monosaccharides
Polysaccharides, made of, Monosaccharides
Monosaccharides, single
Disaccharides, double
Polysaccharides, complex
Carbohydrates, short-term energy
Carbohydrates, breaks down to, Carbon, Hydrogen, Oxygen
""")
g = create_graph(Topic.get("Carbohydrates"), ancestors=False)  # Create and visualize the graph
g.render('bionotes_graph', format='png', view=True)






