'''

The island has eight stations which are connected by a network of teleports;
however, the teleports take a very long time to recharge. This means you can
only use each one once. After you use a teleport, it will shut down and no
longer function. But you can visit any station more than once. For this task,
you should begin at number 1 and try to travel around to all the stations before
returning to the starting point. The map of the teleports is presented as a
string in which the comma-separated list represents teleports. Each teleport is
given the name of the station it connects to. This name consists of two digits,
such as '12' or '32.' Each test requires you to provide a route which passes
through every station. A route is presented as a string of the station numbers
in the sequence in which they must be visited (ex. 123456781).

checkio("12,23,34,45,56,67,78,81") == "123456781"
checkio("12,28,87,71,13,14,34,35,45,46,63,65") == "1365417821"
checkio("12,15,16,23,24,28,83,85,86,87,71,74,56") == "12382478561"
checkio("13,14,23,25,34,35,47,56,58,76,68") == "132586741"

'''

from collections import defaultdict
from itertools import islice

def edges2graph(edges):
    graph = defaultdict(list)
    for n1, n2 in [e for e in edges.split(',')]:
        graph[n1].append(n2)
        graph[n2].append(n1)
    return graph

def dfs_iter(graph, root):
    visited = []
    stack = [root,]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend([x for x in graph[node] if x not in visited])
    return visited

def nodes2path(edges, nodes):
    z = (islice(nodes, i, None) for i in range(2))
    return list(i for i in zip(*z))


def checkio(edges):
    graph = edges2graph(edges)
    edges = [tuple(e) for e in edges.split(',')]
    print "edges = ", edges
    vnodes = dfs_iter(graph, '1')


def checkio(graph):
    queue = [(initial_state(graph), "")]  # state and path
    goal = set("12345678")  # visited stations
    closed = set()
    while queue:
        current_state, path = queue.pop()  # the last element for DFS, the first for BFS
        # let's state is a tuple where visited states on the first place
        if goal == current_state[0]:
            return path
        if current_state in closed:
            continue
        closed.add(current_state)
        for state, action in neighbours(current_state):
            if state in closed:  # it's not necessary but little helps
                continue
            queue.append((state, path + action))
    return "No way!"





print checkio("12,28,87,71,13,14,34,35,45,46,63,65") #== "1365417821"
exit()

print checkio('12,23,13,34,24,41')
#print checkio("12,23,34,45,56,67,78,81") #== "123456781"
exit()
print checkio("12,23,31")
exit()


print checkio("12,15,16,23,24,28,83,85,86,87,71,74,56") #== "12382478561"
print checkio("13,14,23,25,34,35,47,56,58,76,68") #== "132586741"
