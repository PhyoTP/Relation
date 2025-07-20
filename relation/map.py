from graphviz import Digraph

def create_graph(relator, graph=None, visited=None, drawn_edges=None, depth=None, ancestors=True, descendants=True, relations=True):
    if visited is None:
        visited = set()
    if graph is None:
        graph = Digraph()
    if drawn_edges is None:
        drawn_edges = set()

    if id(relator) in visited:
        return graph

    visited.add(id(relator))
    graph.node(str(id(relator)), label=relator.name)

    # Helper: draw edge only if not already drawn
    def draw_edge(a, b, **kwargs):
        if (a, b) not in drawn_edges and (b, a) not in drawn_edges:
            graph.edge(str(id(a)), str(id(b)), **kwargs)
            drawn_edges.add((a, b))
    if depth is not None:
        if depth <= 0:
            return graph
        depth -= 1
    if descendants:
        # Children: relator → child
        for child in relator.children:
            graph.node(str(id(child)), label=child.name)
            draw_edge(relator, child)
            create_graph(child, graph, visited, drawn_edges, depth)
    if relations:
        # Relations: relator -- dashed link → relation
        for relation in relator.relations:
            graph.node(str(id(relation)), label=relation.name)
            draw_edge(relator, relation, arrowhead='none', style='dashed')
            create_graph(relation, graph, visited, drawn_edges, depth)
    if ancestors:
        # Parents: parent → relator
        for parent in relator.parents:
            graph.node(str(id(parent)), label=parent.name)
            draw_edge(parent, relator)
            create_graph(parent, graph, visited, drawn_edges, depth, ancestors, descendants, relations)

    return graph
