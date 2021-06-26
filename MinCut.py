# randomised contraction algorithm to calculate the min.cut
# of an undirected graph G = (V,E) using an adjacency list
# n := # vertices
# m := # edges
# k := # crossing edges in min.cut (A,B)

# pseudocode
# def MinCut(G):
# while n > 2:
# 1. pick a remaining edge (u,v) uniformly at random
# 2. merge / contract (u,v) into a single vertex
# 3. remove self-loops
#  return cut, k
