from collections import defaultdict
import random
from copy import deepcopy


def ring2graph(rings):
    graph = defaultdict(set)
    for (na, nb) in rings:
        graph[na].add(nb)
        graph[nb].add(na)
    return graph

def mostconnected(graph):
    'returns most connected nodes in a list, in decending order'
    return sorted([(k, len(v)) for k,v in graph.items()], key=lambda x: -x[1])

def random_maxnode(graph):
    'randomly choose a maximum connected note, and its connections'
    max_conn = len(max(graph.values(), key=lambda x: len(x)))
    return random.choice([k for k, v in graph.items() if len(v) == max_conn]), max_conn

def deletenode(graph, node):
    del graph[node]
    for k, v in graph.items():
        if node in v:
            graph[k].remove(node)
    return graph

def break_rings_not_quite_working(rings):
    'represent the config as a graph, greedy algorithm to eliminate most connected ring(node) first'
    g = ring2graph(rings)

    nd = 0
    while True:
        l = mostconnected(g)
        node, connections = l[0]
        print "g=", g
        print "l=", l
        # what if there are multiple nodes with equal connections, which to delete
        #   the selected deletion should result in a more balanced disconnected graph
        if connections >= 1:
            deletenode(g, node)
            nd += 1
            print "delete=", node, nd, "\n\n"
        else:
            return nd

def onetry(g):
    nd = 0
    g = deepcopy(g)
    while True:
        node, connections = random_maxnode(g)
        if connections > 0:
            print "delete=", mostconnected(g), node, nd, "\n\t", g
            deletenode(g, node)
            nd += 1

        else:
            print "\n=done=\n"
            return nd

def break_rings_pseudorandom(rings):
    'represent the config as a graph, greedy algorithm to eliminate most connected ring(node) first'
    g = ring2graph(rings)
    results = [onetry(g) for _ in range(1)]
    return min(results)

def break_rings(rings):
    'create maximum number of X-Y-Z type of configuration'
    pass

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    print break_rings(({3,4},{5,6},{2,7},{1,5},{2,6},{8,4},{1,7},{4,5},{9,5},{2,3},{8,2},{2,4},{9,6},{5,7},{3,6},{1,3},)) == 5
    exit()
    print break_rings(({1,2}, {2,3}, {3,4},{4,5},{5, 6}, {6,7})) # should be 3
    exit()
    assert break_rings(({1,9},{1,2},{8,5},{4,6},{5,6},{8,1},{3,4},{2,6},{9,6},{8,4},{8,3},{5,7},{9,7},{2,3},{1,7})) == 5
    assert break_rings(({1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {4, 6})) == 3, "example"
    assert break_rings(({1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4})) == 3, "All to all"
    assert break_rings(({5, 6}, {4, 5}, {3, 4}, {3, 2}, {2, 1}, {1, 6})) == 3, "Chain"
    assert break_rings(({8, 9}, {1, 9}, {1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {8, 7})) == 5, "Long chain"
