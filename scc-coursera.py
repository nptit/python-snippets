__author__ = 'qxu'

import sys
import time
#import resource
from itertools import groupby
from collections import defaultdict
import threading



sys.setrecursionlimit(10 ** 8)
#threading.stack_size(67108864*3)
#resource.setrlimit(resource.RLIMIT_STACK, (2 ** 29, 2 ** 30))


class Track(object):
    """Keeps track of the current time, current source, component leader,
    finish time of each node and the explored nodes."""

    def __init__(self):
        self.current_time = 0
        self.current_source = None
        self.leader = {}
        self.finish_time = {}
        self.explored = set()


def readgraph2hash(filename="SCC.txt"):
    # read adjacent list representation graph into a hash dict
    g = defaultdict(list)
    with open(filename) as f:
        lines = f.readlines()

    nodes=set()
    for l in lines:
        k, v = map(int, l.split())
        g[k].append(v)
        nodes.add(v)

    # add nodes with no outgoing edges
    for n in nodes:
        if n not in g:
            g[n] = []

    return g


def transpose(g):
    # given a directed graph g
    # transpose the graph by reversing all edge directions
    rg = defaultdict(list)
    for k, v in g.items():
        for x in v:
            rg[x].append(k)
    return rg

def dfs(graph_dict, node, track):
    """Inner loop explores all nodes in a SCC. Graph represented as a dict,
    {tail node: [head nodes]}. Depth first search runs recrusively and keeps
    track of the parameters"""

    track.explored.add(node)
    track.leader[node] = track.current_source
    for head in graph_dict[node]:
        if head not in track.explored:
            dfs(graph_dict, head, track)
    track.current_time += 1
    track.finish_time[node] = track.current_time


def dfs_loop(graph_dict, nodes, track):
    """Outter loop checks out all SCCs. Current source node changes when one
    SCC inner loop finishes."""

    for node in nodes:
        if node not in track.explored:
            track.current_source = node
            dfs(graph_dict, node, track)


def scc(graph, reverse_graph, nodes):
    """First runs dfs_loop on reversed graph with nodes in decreasing order,
    then runs dfs_loop on orignial graph with nodes in decreasing finish
    time order(obatined from firt run). Return a dict of {leader: SCC}."""

    out = defaultdict(list)
    track = Track()
    dfs_loop(reverse_graph, nodes, track)
    sorted_nodes = sorted(track.finish_time,
                          key=track.finish_time.get, reverse=True)
    track.current_time = 0
    track.current_source = None
    track.explored = set()
    dfs_loop(graph, sorted_nodes, track)
    for lead, vertex in groupby(sorted(track.leader, key=track.leader.get),
                                key=track.leader.get):
        out[lead] = list(vertex)

    return out


if __name__ == "__main__":
    g = readgraph2hash("scc3.txt")
    rg = transpose(g)
    out = scc(g, rg, g.keys())
    print sorted([len(v) for v in out.values()], reverse=True)[:5]