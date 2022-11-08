import random
import numpy as np
import matrix_gen as mg
import graph_vis as gv

def in_graph(G, a, b):
    if G.shape[0] < (a+1) or G.shape[0] < (b+1):
        print("Vertex index out of bounds!")
        return False
    return True

def connected(G, a, b):
    if not in_graph(G, a, b):
        return
    if a == b:
        return True
    matrix_len = G.shape[0]
    if G[a, b] == 1:
        return True
    G_1 = G
    for i in range(1, matrix_len):
        G_1 = np.matmul(G_1, G)
        if G_1[a, b] >= 1:
            return True
    return False

def same_comp(G, s, a):
    """Returns true if a is in the same connected components as vertices in set s. 
    G is the graph, s is a set, a is a vertex"""
    for x in s:
        if connected(G, a, x):
            return True
        return False

def conn_comps(G):
    # If an upper triangular matrix is passed in as an argument, uncomment the following line of code (35):
    G = G + np.transpose(G)
    matrix_len = G.shape[0]
    comps = []
    if len(comps) == 0:
        x = {0}
        comps.append(x)
    for i in range(1, matrix_len):
        t = 0
        for aset in comps:
            if same_comp(G, aset, i):
                aset.add(i)
                t = 1
                break
        if t == 0:
            y = {i}
            comps.append(y)
    return len(comps)

if __name__ == "__main__":
    # M = np.array([[0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], \
    #     [0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0]])
    # print(M + np.transpose(M))
    # print(conn_comps(M))
    # G = gv.GraphVisualization()
    # G.addEdges(M)

    m = mg.randomMatrix(7)
    print(m + np.transpose(m))
    print(conn_comps(m))
    g = gv.GraphVisualization()
    g.addEdges(m)

    # G.visualize()
    g.visualize()