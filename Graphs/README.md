# **Graph Algorithms**
## **Minimum Spanning Tree (MST)**
### **Prim Algorithm**
* Time complexity : $\cal{O}$ $(V^2)$
#### **Kruskal's Algorithm**
* Algorithm
  * Sort all edges in ascending order by their lengths.
  * Choose the edge with the least length.
  * Add to MST if the nodes consisting of the edge are from distinct *disjoint sets* : *<u>Union-Find</u>*
  * Continue if the nodes originate from the same *disjoint set*
  * Iterate
* Time complexity : $\cal{O}$ $(E \log E)$
* Useful for *sparse graphs* with relatively less $E$ compared with $V^2$
