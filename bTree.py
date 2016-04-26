class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left  = left
        self.right = right

    def __repr__(self):
        return str(self.data)

t3 = Tree(3, Tree(7), Tree(8))
t1 = Tree(1, t3, Tree(4))
t2 = Tree(2, Tree(5), Tree(6))
t0 = Tree(0, t1, t2)


T = Tree('F', Tree('B', Tree('A'), Tree('D', Tree('C'), Tree('E'))), Tree('G', None, Tree('I', Tree('H'), None)))

from collections import OrderedDict
def bfsTree(tree):
    queue = [(0, tree)]
    result = OrderedDict()

    while queue:
        level, node = queue.pop(0)
        if level in result:
            result[level].append(node.data)
        else:
            result[level] = [node.data]

        if node.left:
            queue.append((level+1, node.left))
        if node.right:
            queue.append((level+1, node.right))

    return result


def treeHeight(tree):
    if not tree:
        return 0
    return 1 + max(treeHeight(tree.left), treeHeight(tree.right))

def inOrderTraversePrint(tree):
    if tree:
        inOrderTraversePrint(tree.left)
        print tree.data
        inOrderTraversePrint(tree.right)

def inOrderTraverse(tree):
    if tree:
        return inOrderTraverse(tree.left) + [tree.data] + inOrderTraverse(tree.right)
    else:
        return []

def preOrderTraverse(tree):
    if tree:
        return [tree.data] + inOrderTraverse(tree.left) + inOrderTraverse(tree.right)
    else:
        return []

def dfsTreeTraverse(tree):
    '''traverse tree using DFS'''
    stack = [tree]
    while stack:
        print stack,
        node = stack.pop()
        ## pre-order
        print node.data
        l, r = node.left, node.right
        if r:
            stack.append(r)
        if l:
            stack.append(l)

def maxLengthPaths(tree, path=None):
    '''output pathes with max height'''
    stack = [(0, tree)]
    maxlevel = 0
    while stack:
        print stack,
        level, node = stack.pop()
        ## pre-order
        print node.data
        l, r = node.left, node.right
        maxlevel = max(maxlevel, level)
        if r:
            stack.append((level+1, r))
        if l:
            stack.append((level+1, l))

    return maxlevel

def maxValue(tree):
    ''' find maximum value in a binary tree'''
    if not tree:
        return -float('Inf')
    return max(maxValue(tree.left), tree.data, maxValue(tree.right))

# print bfsTree(t0).values()
# print treeHeight(t0)
# print inOrderTraverse(t0), preOrderTraverse(t0)
# inOrderTraversePrint(t0)
#print treeHeight(T)
print maxLengthPaths(T)
print maxValue(t0)
