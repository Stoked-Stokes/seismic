import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

class GraphVisualization:
   
    def __init__(self):
          
        # visual is a list which stores all 
        # the set of edges that constitutes a
        # graph
        self.visual = []
          
    # addEdge function inputs the vertices of an
    # edge and appends it to the visual list
    def addEdges(self, m):
        n = m.shape[0]
        for i in range(n):
            for j in range(n):
                if i < j and m[i][j] == 1:
                    self.visual.append([i, j])
          
    # In visualize function G is an object of
    # class Graph given by networkx G.add_edges_from(visual)
    # creates a graph with a given list
    # nx.draw_networkx(G) - plots the graph
    # plt.show() - displays the graph
    def visualize(self):
        G = nx.Graph()
        G.add_edges_from(self.visual)
        nx.draw_networkx(G)
        plt.show()

if __name__ == "__main__":
    m = np.array([[0, 0, 1, 0, 0, 0, 1], [0, 0, 0, 1, 1, 1, 1], [0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 1], \
        [0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0]])
    G = GraphVisualization()
    G.addEdges(m)
    G.visualize()