from openktn.ktn import Node

class Component():

    def __init__(self, nodes=None, index=None):

        self.n_nodes=0
        self.n_edges=0

        self.name=None
        self.index=index
        self.node=set()
        self.edge=set()
        self.weight=0.0
        self.probability=0.0

        self.symmetrized=False
        self.T_arrays=None

        if nodes is not None:
            self.add_nodes(nodes)

    def add_nodes(self, nodes):

        if type(nodes)==Node:
            nodes=[nodes]

        for node in nodes:

            node.component=self
            self.node.add(node)
            self.edge.union(set(node.edge.values()))
            self.weight+=node.weight
            self.probability+=node.probability

        self.n_nodes=len(self.node)
        self.n_edges=len(self.edge)


