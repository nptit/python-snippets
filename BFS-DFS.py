# http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/

def DFS_recursive(graph, start, visited=None):
	if not visited:
		visited = [start]
		print 'visit: ', start

	for v in graph[start]:
		if v not in visited:
			visited.append(v)
			print "visit: ", v
			DFS_recursive(graph, v, visited)
	return visited

## test
graph1 = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

print DFS_recursive(graph1, 'A')

graph2 = {0:[1,2,3], 1:[5,6], 2:[4], 3:[2,4], 4:[1], 5:[], 6:[4]}

print DFS_recursive(graph2, 0)

#http://www.cs.toronto.edu/~heap/270F02/node36.html
def DFS_stack(graph, start):
	stack = [start]
	visited = []
	while stack:
		v = stack.pop()
		if v not in visited:
			visited.append(v)

		for w in graph[v]:
			if w not in visited:
				stack.append(w) 

	return visited


print DFS_stack(graph2, 0)


def dfs_stack(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

print dfs_stack(graph1, 'A')


def bfs(graph, start):
    visited, queue = [], [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)
        for v in graph[vertex]:
        	if v not in visited:
	            queue.append(v)
    return visited

print bfs(graph1, 'A') # {'B', 'C', 'A', 'F', 'D', 'E'}




def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

dfs(graph1, 'C') # {'E', 'D', 'F', 'A', 'C', 'B'}





def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))


print list(dfs_paths(graph1, 'A', 'F')) # [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]

# def dfs_paths(graph, start, goal, path=None):
#     if path is None:
#         path = [start]
#     if start == goal:
#         yield path
#     for next in graph[start] - set(path):
#         yield from dfs_paths(graph, next, goal, path + [next])

# list(dfs_paths(graph, 'C', 'F')) # [['C', 'F'], ['C', 'A', 'B', 'E', 'F']]






def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

print bfs(graph1, 'A') # {'B', 'C', 'A', 'F', 'D', 'E'}


def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

print list(bfs_paths(graph1, 'A', 'F')) # [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]

def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None

print shortest_path(graph1, 'A', 'F') # ['A', 'C', 'F']

