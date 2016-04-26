from collections import defaultdict


def check_connection(network, first, second):
    # convert it in a graph represented by a dict
    net = defaultdict(set)
    for pair in network:
        p1, p2 = pair.split('-')
        net[p1].add(p2)
        net[p2].add(p1)

    # BFS search
    queue = [first]
    visited = set()
    while queue:
        v = queue.pop(0)
        if v not in visited:
            visited.add(v)
        for ni in net[v]:
            if ni not in visited:
                queue.append(ni)

    return True if second in visited else False


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "1. Scout Brotherhood"

    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "2. Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "3. I don't know any scouts."
