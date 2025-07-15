# What is BFS?
- It is a graph traversal technique.
- Popular algorithms like Dijkstra’s shortest path, Kahn’s Algorithm, and Prim’s algorithm are based on BFS.
- BFS itself can be used to detect cycle in a directed and undirected graph, find shortest path in an unweighted graph and many more problems.

---
# Working
![[BFS_aifl.excalidraw|500]]

****Explanation:**** Starting from 0, the BFS traversal will follow these steps:  
- Visit 0 → Output: 0  
- Visit 2 (first neighbor of 0) → Output: 0, 2  
- Visit 3 (next neighbor of 0) → Output: 0, 2, 3  
- Visit 1 (next neighbor of 0) → Output: 0, 2, 3, 1  
- Visit 4 (neighbor of 2) → Final Output: 0, 2, 3, 1, 4

---
# Code Explained
![[BFS_aifl_Solving.excalidraw|1000]]

---
# Code Implementation
``` python
from collections import defaultdict


# This class represents a directed graph
# using adjacency list representation
class Graph:

    # Constructor
    def __init__(self):

        # Default dictionary to store graph
        self.graph = defaultdict(list)

    # Function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # Function to print a BFS of graph
    def BFS(self, s):

        # Mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)

        # Create a queue for BFS
        queue = []

        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:

            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            print(s, end=" ")

            # Get all adjacent vertices of the
            # dequeued vertex s.
            # If an adjacent has not been visited,
            # then mark it visited and enqueue it
            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

# Driver code
if __name__ == '__main__':

    # Create a graph given in
    # the above diagram
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print("Following is Breadth First Traversal"
        " (starting from vertex 2)")
    g.BFS(2)
```

``` text
Output: 2 0 3 1
```

---
# Complexity
- **Time Complexity** : `O(V+E)` ---> V is number of vertices and E is the number of edges
- **Auxiliary Space Complexity** : `O(V)`

---
# Python Code Explanation
### Import
- `defaultdict` ---> Normal dictionary, but if you access a key that doesn't exist yet, it creates a default value (empty list).

### Graph
- **Graph** will be directed from **node u** to **node v**.
- Represent Graph as an **adjacency list**, which means for every vertex, we store a list of vertices it points to.