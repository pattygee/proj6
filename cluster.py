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

    def addedge(self,edge):
       x = edge[0]
       y = edge[1]
       self.degree[x][x] += 1
       self.degree[y][y] += 1
       self.adjacency[x][y] += 1
       self.adjacency[y][x] += 1
       self.laplacian = np.subtract(self.degree, self.adjacency)

    def laplacianmatrix(self) -> np.array:
        return self.laplacian

    def fiedlervector(self) -> np.array:
        eigenvalues, eigenvectors = np.linalg.eig(self.laplacian)
        f_val = np.sort(eigenvalues)[1]
        f_val_index = np.where(eigenvalues == f_val)[0][0]
        f_vec = eigenvectors[:, f_val_index]
        return f_vec if f_vec[0] > 0 else -1 * f_vec

    def clustersign(self):
        pos_indices = []
        neg_indices = []
        f_vec = self.fiedlervector()
        for i in range(len(f_vec)):
            if f_vec[i] < 0:
                neg_indices.append(i)
            else:
                pos_indices.append(i)

        return [pos_indices, neg_indices]