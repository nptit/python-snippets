__author__ = 'qxu'

def rDFSall(g):
    g = initalize(g)
    for w in g.keys():
        if g[w][1] is None:
            rDFS(g, w)
    return g

# nonrecursive implementation
def DFS(g):
    g = initalize(g)
    i = 0
    for v in g.keys():
        stack = list()
        stack.append(v)
        while len(stack) > 0:
            x = stack.pop()
            if g[x][1] is None:
                g[x][1] = i
                i += 1
                for node in g[x][0]:
                    stack.append(node)
    return g

def DFSn(g):
    # return a hash
    # key: node
    # value: order of the node is traversed during DFS, from 0 to len(g)-1
    i = 0
    dn = defaultdict()
    for v in g.keys():
        stack = list()
        stack.append(v)
        while len(stack) > 0:
            x = stack.pop()
            if x not in dn:
                dn[x] = i
                i += 1
                for node in g[x]:
                    stack.append(node)
    return dn

def DFSf(g):
    # return a hash
    # key: node
    # value: finishing time of each node
    t = 0
    finish_time = defaultdict()
    visited = []

    for v in g.keys():
        if v not in visited:
            print dfs_iter(g, v, visited, t, finish_time)
    print finish_time



def dfs_iter(g, v, visited, t, finish_time):
    stack = [v, ]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend([x for x in g[node] if x not in visited])

    t += 1
    finish_time[v] = t
    return visited

