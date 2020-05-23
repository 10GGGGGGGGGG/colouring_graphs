import networkx as nx
import matplotlib.pyplot as plt


# Python program for solution of M Coloring
# problem using backtracking

class Graph():
    nodes = []
    edges = []
    matrix = []
    colors = []
    colorDB = ['red','aqua','lawngreen','yellow','pink','orange','gray','salmon','cornflowerblue','fuchsia','c']

    def __init__(self, nodes):
        self.nodes = nodes
        self.colors = [None] * len(self.nodes)


    def colorearGrafo(self, m):
        if self.colorearRecursivo(m, 0) == None:
            print("No hay solución para ese número máximo de colores.")
            return False

        # Print the solution
        print("Existe solución para ese número máximo de colores. \nLa asignación es la siguiente:")
        for i in range(len(self.nodes)):
            print('vértice ',self.nodes[i],': (',self.colors[i]+1,')',self.colorDB[self.colors[i]])
        return True

    def colorearRecursivo(self, m, v):
        if v == len(self.nodes):
            return True

        for c in range(m):
            if self.checkValido(v, c):
                self.colors[v] = c
                if self.colorearRecursivo(m, v + 1):
                    return True
                self.colors[v] = None

    def checkValido(self, v, c):
        for i in range(len(self.nodes)):
            if self.matrix[v][i] == 1 and self.colors[i] == c:
                return False
        return True


    def loadEdges(self, edgesMatrix):
        self.matrix = edgesMatrix
        for row in range(len(self.nodes)):
            for col in range(len(self.nodes)):
                if edgesMatrix[row][col]==1:
                    self.edges.append((self.nodes[row],self.nodes[col]))

        print(self.edges)

    def dibujarGrafo(self):
        G = nx.Graph()
        labels = {}
        for n in self.nodes:
            labels[n] = n

        G.add_nodes_from(self.nodes)
        G.add_edges_from(self.edges)

        pos = nx.circular_layout(G)

        for i in range(len(self.nodes)):
            nx.draw_networkx_nodes(G, pos,
                               nodelist=[self.nodes[i]],
                               node_color=self.colorDB[self.colors[i]],
                               node_size=500,
                               alpha=0.7)

        nx.draw_networkx_labels(G, pos, labels, font_size=18)
        nx.draw_networkx_edges(G, pos,
                               edgelist=G.edges,
                               width=1.5, alpha=1, edge_color='black')
        plt.show()





#'''
g = Graph(['a','b','c','d','e','f','g'])
g.loadEdges([   #a  b  c  d  e  f  g
                [1, 0, 1, 0, 1, 0, 1],# a
                [0, 1, 1, 1, 1, 0, 1],# b
                [1, 1, 1, 1, 1, 1, 1],# c
                [0, 1, 1, 1, 0, 1, 1],# d
                [1, 1, 1, 0, 1, 1, 1],# e
                [0, 0, 1, 1, 1, 1, 1],# f
                [1, 1, 1, 1, 1, 1, 1] # g
             ])
m = 7
g.colorearGrafo(m)
g.dibujarGrafo()

'''
g = Graph(['a','b','c','d'])
g.loadEdges([
                #a  b  c  d
                [1, 1, 1, 1],# a
                [1, 1, 1, 1],# b
                [1, 1, 1, 1],# c
                [1, 1, 1, 1] # d
             ])
m = 4
g.colorearGrafo(m)
g.dibujarGrafo()
'''
