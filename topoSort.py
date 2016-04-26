
g = {'A':['B','D'],'B':['C'], 'C':['D','E'], 'D':['E'],'E':[],'F':[]}

def inDegree(g, node):
    '''return indegree given a node in graph g'''
    indegree = 0
    for n, d in g.items():
        for des in d:
            if des == node:
                indegree += 1
    return indegree

def getZeroIndegree(arr):
    for node, inDegree in arr:
        if inDegree == 0:
            return node
    if arr:
        raise Exception('Cyclic graph?')


def topoSort(g):
    indegrees = [(node, inDegree(g, node)) for node in g]


