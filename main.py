
import  graphs


maps=  graphs.wGraph()

for x in range(0,5):
  maps.addNodes(x)



maps.addEdges(0,1,1)
maps.addEdges(0,2,2)
maps.addEdges(0,3,3)
maps.addEdges(1,2,1)
maps.addEdges(1,4,3)
maps.BreadthFirstSearch(0)

