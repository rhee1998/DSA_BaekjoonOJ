# **Graph Algorithms (Alphabetical Order)**

## **Bellman-Ford Algorithm**
#### **Usage**
* Searches for minimum distance paths from one node to other nodes
* Compatible with *directional graphs* containing negative-valued edges $\rightarrow$ *negative cycle detection*

#### **Algorithm**
1. Initialize minimum distance array with a sufficiently large number `INF`
2. For each *edge* starting from `s` to `e`, update *minimum distance* for `e`
3. Iterate $V$ times
4. If *minimum distance array* is updated in the last iteration, *negative cycle* exists

#### **Computational Complexity**
* Time complexity : $\cal{O}$ $(VE)$ for all cases

#### **Function(s)**
`def BellmanFord(start, N, graph, dist, INF=10**30)`
* Input(s)
* Output(s)

  //TODO

## **Dijkstra's Algorithm**
### **1. $\cal{O}$ $(V^2)$ Solution**
#### **Algorithm**
1. Initialize minimum distances `dists` from *start node* to other nodes by `INF`, a sufficiently large number
2. Select the node with the least minimum distance from *start node* as *current node*
3. For each node adjacent to *current node*, update `dists` if possible
4. Iterate

### **2. $\cal{O}$ $((V + E) \log V)$ Solution**
#### **Algorithm**
* Implements *priority queue* for efficient searching of the node with least minimum distance

#### **Function(s)**
`def Dijkstra(start, N, G, INF=10**30)`
* Input(s)
  * `start (int)` : Starting node ID
  * `N (int)` : Number of nodes in graph, each labeled from `0` to `N - 1`
  * `G (int)` : "`a` $\rightarrow$ `b` at cost `c`" encoded as `G[a].append((b, c))`
* Output(s)
  * `dists (list)` : List of minimum distances from `start` to each node

`def DijkstraPath(start, N, G, INF=10**30)`
* Input(s) : same with `Dijkstra(start, N, G, INF=10**30)`
* Output(s)
  * `dists (list)` : List of minimum distances from `start` to each node
  * `paths (list)` : One of minimum distance paths from `start` to each node


## **Minimum Spanning Tree (MST)**
### **1. Kruskal's Algorithm**
#### **Usage**
* Finds a connected subgraph (tree) that has the least sum of edge values
* Useful for *sparse graphs* with relatively less $E$ compared with $V^2$

#### **Algorithm**
1. Sort all edges in ascending order by their lengths.
2. Choose the edge with the smallest length.
3. Add to MST if the nodes consisting of the edge are from distinct *disjoint sets* : *<u>Union-Find</u>*
4. Continue if the nodes originate from the same *disjoint set*
5. Iterate

#### **Computational Complexity**
* Time complexity : $\cal{O}$ $(E \log E)$


### **2. Prim's Algorithm**
#### **Usage**
* Finds a connected subgraph (tree) that has the least sum of edge values
* Useful for *dense graphs* with relatively large $E$ where it is comparable to $V^2$

#### **Algorithm**
1. Choose a random node to start
2. Choose an edge with the smallest length from the edges connected to the visited node(s)
3. Add the new node to the set of visited node(s)
4. Iterate

#### **Computational Complexity**
* Time complexity : $\cal{O}$ $(V^2)$


## **Union-Find**
//TODO
