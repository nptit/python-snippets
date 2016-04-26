from collections import defaultdict


def checkio(edges):
    # convert it in a graph represented by a dict
    net = defaultdict(set)
    for pair in edges.split(','):
        p1, p2 = list(pair)
        net[p1].add(p2)
        net[p2].add(p1)

    # DFS search
    stack = ['1']
    visited = list()
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
        for ni in net[v]:
            if ni not in visited:
                stack.append(ni)

    return visited


if __name__ == '__main__':
    print checkio("12,23,34,45,56,67,78,81") #== "123456781"
    print checkio("12,28,87,71,13,14,34,35,45,46,63,65") #== "1365417821"
    print checkio("12,15,16,23,24,28,83,85,86,87,71,74,56") #== "12382478561"
    print checkio("13,14,23,25,34,35,47,56,58,76,68") #== "132586741"


