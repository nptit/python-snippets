# 6.00.2x Problem Set 5
# Graph optimization
#
# A set of data structures to represent graphs
#

class Node(object):
    def __init__(self, name):
        self.name = str(name)
    def getName(self):
        return self.name
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
    def __eq__(self, other):
        return self.name == other.name
    def __ne__(self, other):
        return not self.__eq__(other)
    def __hash__(self):
        # Override the default hash method
        # Think: Why would we want to do this?
        return self.name.__hash__()

class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return '{0}->{1}'.format(self.src, self.dest)

class Digraph(object):
    """
    A directed graph
    """
    def __init__(self):
        # A Python Set is basically a list that doesn't allow duplicates.
        # Entries into a set must be hashable (where have we seen this before?)
        # Because it is backed by a hashtable, lookups are O(1) as opposed to the O(n) of a list (nifty!)
        # See http://docs.python.org/2/library/stdtypes.html#set-types-set-frozenset
        self.nodes = set([])
        self.edges = {}

    def addNode(self, node):
        if node in self.nodes:
            # Even though self.nodes is a Set, we want to do this to make sure we
            # don't add a duplicate entry for the same node in the self.edges list.
            raise ValueError('Duplicate node')
        else:
            self.nodes.add(node)
            self.edges[node] = []

    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)

    def childrenOf(self, node):
        return self.edges[node]

    def hasNode(self, node):
        return node in self.nodes

    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[str(k)]:
                res = '{0}{1}->{2}\n'.format(res, k, d)
        return res[:-1]

# Problem 1
class WeightedEdge(Edge):
    def __init__(self, src, dest, w1, w2):
        self.src = src
        self.dest = dest
        self.w1 = w1
        self.w2 = w2

    def getTotalDistance(self):
        return self.w1

    def getOutdoorDistance(self):
        return self.w2

    def __str__(self):
        return str(self.src) + '->' + str(self.dest) +' (' + str(self.w1) + ', ' + str(self.w2) + ')'


class WeightedDigraph(Digraph):
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        w1 = edge.w1
        w2 = edge.w2
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append([dest, (float(w1), float(w2))])

    def childrenOf(self, node):
        return [e[0] for e in self.edges[node]]

    def __str__(self):
        res = ''
        for k in self.edges:
            for d, (w1, w2) in self.edges[k]:
                res = '{0}{1}->{2} ({3}, {4})\n'.format(res, k, d, w1, w2)
        return res[:-1]

if __name__ == '__main__':
    nh = Node('h')
    nj = Node('j')
    nk = Node('k')
    nm = Node('m')
    ng = Node('g')
    g = WeightedDigraph()
    g.addNode(nh)
    g.addNode(nj)
    g.addNode(nk)
    g.addNode(nm)
    g.addNode(ng)
    randomEdge = WeightedEdge(nj, nh, 56, 19)
    g.addEdge(randomEdge)
    randomEdge = WeightedEdge(nm, nh, 83, 40)
    g.addEdge(randomEdge)
    randomEdge = WeightedEdge(nh, nj, 63, 41)
    g.addEdge(randomEdge)
    randomEdge = WeightedEdge(nh, nj, 27, 5)
    g.addEdge(randomEdge)
    randomEdge = WeightedEdge(nj, nk, 57, 55)
    g.addEdge(randomEdge)
    randomEdge = WeightedEdge(nj, nk, 49, 32)
    g.addEdge(randomEdge)
    randomEdge = WeightedEdge(nm, nk, 27, 20)
    g.addEdge(randomEdge)
    randomEdge = WeightedEdge(nk, nj, 23, 12)
    g.addEdge(randomEdge)
    print g.childrenOf(nh)
    print g.childrenOf(nj)

# g = WeightedDigraph()
# na = Node('a')
# nb = Node('b')
# nc = Node('c')
# g.addNode(na)
# g.addNode(nb)
# g.addNode(nc)
# e1 = WeightedEdge(na, nb, 15, 10)
# e2 = WeightedEdge(na, nc, 14, 6)
# e3 = WeightedEdge(nb, nc, 3, 1)
# #print e1, e2, e3
# g.addEdge(e1)
# g.addEdge(e2)
# g.addEdge(e3)

# #print g.edges
# #print g

# na = Node('a')
# nb = Node('b')
# nc = Node('c')
# e1 = WeightedEdge(na, nb, 15, 10)
# print isinstance(e1, Edge) #: True
# print isinstance(e1, WeightedEdge) #: True
# print e1.getSource() #: a
# print e1.getDestination() #: b
# print e1.getTotalDistance() #: 15.0
# print e1.getOutdoorDistance() #: 10.0


