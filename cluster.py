from __future__ import annotations
import json
import math
from typing import List
import numpy as np

class Graph():
    def  __init__(self,
            nodecount : None):
        self.nodecount = nodecount
        self.degree = [[0 for i in range(nodecount)] for j in range(nodecount)]
        self.adjacency = [[0 for i in range(nodecount)] for j in range(nodecount)]

    # Add an edge to the Laplacian matrix.
    # An edge is a pair [x,y].
    def addedge(self,edge):
       x = edge[0]
       y = edge[1]
       self.degree[x][x] += 1
       self.degree[y][y] += 1
       self.adjacency[x][y] += 1
       self.adjacency[y][x] += 1
       self.laplacian = np.array([list(map(lambda x, y: x - y, self.degree[i], self.adjacency[i])) for i in range(self.nodecount)], dtype = np.single)

    # Don't change this - no need.
    def laplacianmatrix(self) -> np.array:
        return self.laplacian

    # Calculate the Fiedler vector and return it.
    # You can use the default one from np.linalg.eig
    # but make sure the first entry is positive.
    # If not, negate the whole thing.
    def fiedlervector(self) -> np.array:
        # Replace this next line with your code.
        fvec = [0]
        # Return
        return fvec

    # Cluster the nodes.
    # You should return a list of two lists.
    # The first list contains all the indices with nonnegative (positive and 0) Fiedler vector entry.
    # The second list contains all the indices with negative Fiedler vector entry.

    def clustersign(self):
        # Replace the next two lines with your code.
        pind = []
        nind = []
        # Return
        return([pind,nind])