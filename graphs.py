# graph Data Structure

from collections import deque


class Graph:

    def __init__(self):
        self.num_nodes = 0
        self.adjacentList = {}

    # adding nodes to the list
    def addNodes(self, node):
        self.adjacentList[node] = []
        self.num_nodes += 1
        return True

    def addEdges(self, node_1, node_2):
        self.adjacentList[node_1].append(node_2)
        self.adjacentList[node_2].append(node_1)
        return True

    def BFS(self, root):
        if (self.adjacentList[root] == None):
            raise ('Wrong node you picket fool')
        visited = set()
        queue = deque([root])

        while queue:
            #pops the item and adds it in the  visited set.
            vertex = queue.popleft()
            visited.add(vertex)

            for i in self.adjacentList[vertex]:
                if i not in visited:
                    queue.append(i)

        print(visited)

    def DFS(self, root, visited):
        if (root is None): raise (' No root given')
        if root not in visited:
            visited.add(root)
            print(root)
            for neighbour in self.adjacentList[root]:
                self.DFS(neighbour, visited)

    def ShowNodes(self):
        return self.adjacentList
