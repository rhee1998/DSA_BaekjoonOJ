# **Graph Algorithms**
### **Minimum Spanning Tree (MST)**
##### **Prim Algorithm**
* Time complexity : $\cal{O}$ $(V^2)$
##### **Kruskal's Algorithm**
* Algorithm
  1. Sort all edges in ascending order by their lengths.
  2. Choose the edge with least length.
  3. Add to MST if the nodes consisting the edge is from distinct *disjoint sets* : *<u>Union-Find</u>*
  4. Continue if the nodes originate from the same *disjoint set*\
  5. Iterate
</br>
* Time complexity : $\cal{O}$ $(E \log E)$
* Useful for *sparse graphs* with relatively less $E$ compared with $V^2$
