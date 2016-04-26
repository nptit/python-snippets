__author__ = 'qxu'

'''
The file contains the edges of a directed graph. Vertices are labeled as positive integers from 1 to 875714. Every row
indicates an edge, the vertex label in first column is the tail and the vertex label in second column is the head
(recall the graph is directed, and the edges are directed from the first column vertex to the second column vertex).
So for example, the 11th row looks likes : "2 47646". This just means that the vertex with label 2 has an outgoing
edge to the vertex with label 47646

Your task is to code up the algorithm from the video lectures for computing strongly connected components (SCCs),
and to run this algorithm on the given graph.

Output Format: You should output the sizes of the 5 largest SCCs in the given graph, in decreasing order of sizes,
separated by commas (avoid any spaces). So if your algorithm computes the sizes of the five largest SCCs to be 500,
400, 300, 200 and 100, then your answer should be "500,400,300,200,100". If your algorithm finds less than 5 SCCs,
then write 0 for the remaining terms. Thus, if your algorithm computes only 3 SCCs whose sizes are 400, 300, and 100,
then your answer should be "400,300,100,0,0".

WARNING: This is the most challenging programming assignment of the course. Because of the size of the graph you
may have to manage memory carefully. The best way to do this depends on your programming language and environment,
and we strongly suggest that you exchange tips for doing this on the discussion forums.
'''
from collections import defaultdict

def readgraph2hash(filename="SCC.txt"):
    # read adjacent list representation graph into a hash dict
    with open(filename) as f:
        lines = f.readlines()

    return dict([(line.split()[0], line.split()[1:]) for line in lines])

def transpose(g):
    # given a directed graph g
    # transpose the graph by reversing all edge directions
    rg = defaultdict(list)
    for k, v in g.items():
        for x in v:
            rg[x].append(k)
    return rg

def dfs(g, v, visited, leader, finish_time, t, source):
    visited.add(v)
    leader[v] = source
    for x in g[v]:
        if x not in visited:
            dfs(g, x, visited, leader, finish_time, t, source)

    t += 1
    finish_time[v] = t

def dfs_loop(g):
    t = 0
    leader = defaultdict()
    finish_time = defaultdict()
    visited = set()

    for node in sorted(g.keys(), reverse=True):
        if node not in visited:
            source = node
            dfs(g, node, visited, leader, finish_time, t, source)

    print visited
    print finish_time
    print leader


if __name__ == "__main__":
    g = {1: [7],
                   2: [5],
                   3: [9],
                   4: [1],
                   5: [8],
                   6: [3, 8],
                   7: [4, 9],
                   8: [2],
                   9: [6]
                   }

    # print rDFSall(g)
    print dfs_loop(g)

