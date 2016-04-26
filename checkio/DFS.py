graph = {0:[1,5], 1:[0,2,3], 2:[1,4], 3:[1,4,5], 4:[2,3,5], 5:[0,3,4]}

def dfs_iter(graph, root):
    visited = []
    stack = [root,]

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.append(node)
            stack.extend([x for x in graph[node] if x not in visited])

    return visited


print dfs_iter(graph, 0)


def dfs(graph, root, visited=None):
    if not visited:
        visited = []

    if root in visited:
        return

    visited.append(root)

    for v in [x for x in graph[root] if x not in visited]:
        dfs(graph, v, visited)

    return visited

print dfs(graph,0)


def dfs_path(graph, root, target, path=None):
    if not path:
        path = [root]

    if root == target:
        yield path

    for v in [x for x in graph[root] if x not in path]:
        for eachpath in dfs_path(graph, v, target, path+[v]):
            yield eachpath

print list(dfs_path(graph, 0, 5))



from collections import defaultdict

def edges2graph(edges):
    graph = defaultdict(list)
    for n1, n2 in [e for e in edges.split(',')]:
        graph[n1].append(n2)
        graph[n2].append(n1)
    return graph


def path2nodes(path):
    'give a list of unique node given path, [0, 1], [1,2] --> [0,1,2]'
    r = []
    for p in path:
        x, y = p
        if len(r) >= 2:
            if x == r[-1]:
                r.append(y)
            elif y == r[-1]:
                r.append(x)
            else:
                return 'not a path'
        else:
            r.append(x)
            r.append(y)
    return r
