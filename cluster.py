from __future__ import annotations
import json
import math
from typing import List
import numpy as np

class Graph():
    def  __init__(self,
            nodecount : None):
        self.nodecount = nodecount
        self.degree = np.zeros((nodecount, nodecount))
        self.adjacency = np.zeros((nodecount, nodecount))

    # Add an edge to the Laplacian matrix.
    # An edge is a pair [x,y].
    def addedge(self,edge):
       x = edge[0]
       y = edge[1]
       self.degree[x][x] += 1
       self.degree[y][y] += 1
       self.adjacency[x][y] += 1
       self.adjacency[y][x] += 1
       self.laplacian = np.subtract(self.degree, self.adjacency)

    # Don't change this - no need.
    def laplacianmatrix(self) -> np.array:
        return self.laplacian

    # Calculate the Fiedler vector and return it.
    # You can use the default one from np.linalg.eig
    # but make sure the first entry is positive.
    # If not, negate the whole thing.
    def fiedlervector(self) -> np.array:
        eigenvalues, eigenvectors = np.linalg.eig(self.laplacian)
        f_val = np.sort(eigenvalues)[1]
        f_val_index = np.where(eigenvalues == f_val)[0][0]
        f_vec = eigenvectors[:, f_val_index]
        return f_vec if f_vec[0] > 0 else -1 * f_vec
        

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