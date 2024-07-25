class Node:

    def __init__(self, val=0):
        self.val = val
        self.children = []
        self.isVisited = False


class Graph:

    def __init__(self):
        self.nodes = []

def getRootDFS(start_node, end_node):

    if not start_node:
        return False
    
    start_node.isVisited = True

    for child in start_node.children:
        if not child.isVisited:
            if child == end_node:
                return True
            
            res = False or getRootDFS(child, end_node)
            
        

    return res


def getRootBFS(start_node, end_node):
    queue = []
    queue.append(start_node)
    start_node.isVisited = True


    while len(queue):
        node = queue.pop(0)

        if node == end_node:
            return True
        
        for child in node.children:
            if not child.isVisited:
                queue.append(child)
                child.isVisited = True


    
    return False