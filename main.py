# import arrays as easyProb
# from trees import BinaryTreees
# from linkedList import LinkedList
# from slidingWindow import SubArray_with_given_sum
from graphs import Graph


test= Graph()
test.addNodes(0)
test.addNodes(1)
test.addNodes(2)
test.addNodes(3)
test.addNodes(4)


test.addEdges(0,1)
test.addEdges(0,3)
test.addEdges(0,2)
test.addEdges(1,3)
test.addEdges(3,4)


b=test.ShowNodes()
#b=test.BFS(1)

visited=set()
test.DFS(0,visited)


print(b)

