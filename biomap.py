from pyvis.network import Network
import networkx as nx
from bionotes import bioMolecules

def create_graph():
    nx_graph = nx.Graph()
    def add_relator(relator):
        nx_graph.add_node(str(id(relator)), label=relator.name)
        for child in relator.children:
            nx_graph.add_edge(str(id(relator)), str(id(child)), arrows='to')
            add_relator(child)
        for relation in relator.relations:
            nx_graph.add_edge(str(id(relator)), str(id(relation)), style='dashed')
            add_relator(relation)
        for parent in relator.parents:
            nx_graph.add_edge(str(id(parent)), str(id(relator)), arrows='to')
            add_relator(parent)

    nt = Network()
    # populates the nodes and edges data structures
    nt.from_nx(nx_graph)
    nt.write_html('graph.html')

create_graph()