__author__ = 'qxu'

import random
import math

def readgraph2hash(filename="kargerMincut.txt"):
    # read adjacent list representation graph into a hash dict
    with open(filename) as f:
        lines = f.readlines()

    return dict([(line.split()[0], line.split()[1:]) for line in lines])

def readgraph2tuples(filename="kargerMincut.txt"):
    # read adjacent list representation graph into a list of tuples
    with open(filename) as f:
        lines = f.readlines()

    return [(line.split()[0], line.split()[1:]) for line in lines]


def randomedge(g):
    # given a graph in a hash, choose an edge at random
    # return a tuple of two nodes define an edge

    # convert dict to list of tuples
    t = [(k, e) for k, v in g.items() for e in v]
    # choose one
    return random.choice(t)

def contract(g, t):
    # give a graph dict and an edge (a tuple), delete the edges and return the updated the graph
    nodea, nodeb = t

    # combine the nodes of the merged nodes, and remove themselves
    newk = "-".join(t)
    g[newk] = (g[nodea] + g[nodeb])
    g[newk] = [x for x in g[newk] if x != nodea and x != nodeb]
    # remove the two nodes
    del g[nodea], g[nodeb]
    # update graph/dictionary for nodes pointing to the old nodes
    for v in g[newk]:
        g[v] = [newk if el == nodea or el == nodeb else el for el in g[v]]

    return g

def karger(g):
    # run one attempt of karger's algorithm
    # return min cut
    while len(g.keys()) > 2:
        t = randomedge(g)
        g = contract(g, t)

    return g

def nkarger(g):
    # run n**2*m*log(n) trials time by a scale factor
    nodes = len(g.keys())
    edges = sum(map(lambda x: len(x), g.values()))/2
    # trials = int(nodes**2*edges*math.log(nodes))
    trials = 100
    results = []

    for i in xrange(trials):
        kg = karger(copy.deepcopy(g))
        results.append(len(kg.values()[0]))

    mincut = min(results)

    print "node = ", nodes, " edges= ", edges
    print "trials = ", trials, "mincut = ", mincut
    print "results = ", results

    return mincut

import copy

if __name__ == "__main__":

    # mincut is 2
    g = readgraph2hash(filename="karger-test1.txt")
    # mincut is 2
    g = readgraph2hash(filename="karger-test2.txt")
    # mincut is 3
    g = readgraph2hash(filename="karger-test3.txt")
    # mincut is 9
    g = readgraph2hash(filename="karger-test4.txt")
    # assignment
    g = readgraph2hash()
    nkarger(g)
