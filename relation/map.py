from pyvis.network import Network

def create_graph(relator, net=None, visited=None, drawn_edges=None, depth=None, ancestors=True, descendants=True, relations=True, self_node=True):
    if visited is None:
        visited = set()
    if net is None:
        net = Network(directed=True)
    if drawn_edges is None:
        drawn_edges = set()

    if id(relator) in visited:
        return net
    visited.add(id(relator))

    def node_id(obj):
        return str(id(obj))

    if self_node:
        net.add_node(node_id(relator), label=str(relator), shape="box")

    def draw_edge(a, b, **kwargs):
        key = (id(a), id(b))
        if key not in drawn_edges and (id(b), id(a)) not in drawn_edges:
            net.add_edge(node_id(a), node_id(b), **kwargs)
            drawn_edges.add(key)

    if depth is not None:
        if depth <= 0:
            return net
        depth -= 1

    if descendants:
        for child in relator.children:
            net.add_node(node_id(child), label=str(child), shape="box")
            draw_edge(relator, child, arrows="to")
            create_graph(child, net, visited, drawn_edges, depth, ancestors, descendants, relations)

    if relations:
        for relation in relator.relations:
            net.add_node(node_id(relation), label=str(relation), shape="ellipse")
            draw_edge(relator, relation, arrows="", dashes=True)
            create_graph(relation, net, visited, drawn_edges, depth, ancestors, descendants, relations)

    if ancestors:
        for parent in relator.parents:
            net.add_node(node_id(parent), label=str(parent), shape="box")
            draw_edge(parent, relator, arrows="to")
            create_graph(parent, net, visited, drawn_edges, depth, ancestors, descendants, relations)

    return net
