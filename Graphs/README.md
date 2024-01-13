# **Graph Algorithms (Alphabetical Order)**

## **Dijkstra's Algorithm**
### **1. $\cal{O}$ $(V^2)$ Solution**
* Algorithm
  * Initialize minimum distances `dists` from *start node* to other nodes by `inf`, a sufficiently large number
  * Select the node with the least minimum distance from *start node* as *current node*
  * For each node adjacent to *current node*, update `dists` if possible
  * Iterate

### **2. $\cal{O}$ $((V + E) \log V)$ Solution**
* Implements *priority queue* for efficient searching of the node with least minimum distance

## **Minimum Spanning Tree (MST)**
### **1. Kruskal Algorithm**
* Algorithm
  * Sort all edges in ascending order by their lengths.
  * Choose the edge with the smallest length.
  * Add to MST if the nodes consisting of the edge are from distinct *disjoint sets* : *<u>Union-Find</u>*
  * Continue if the nodes originate from the same *disjoint set*
  * Iterate
* Time complexity : $\cal{O}$ $(E \log E)$
* Useful for *sparse graphs* with relatively less $E$ compared with $V^2$

### **2. Prim Algorithm**
* Algorithm
  * Choose a random node to start
  * Choose an edge with the smallest length from the edges connected to the visited node(s)
  * Add the new node to the set of visited node(s)
  * Iterate
* Time complexity : $\cal{O}$ $(V^2)$
* Useful for *dense graphs* with relatively large $E$ where it is comparable to $V^2$



