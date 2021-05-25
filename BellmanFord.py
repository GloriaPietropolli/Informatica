"""
BELLMAN FORD ALGORITHM
we have to implement again the class because now we are considering weighted vertex
"""


class Graph_BF:

    def __init__(self, numero_nodi):
        self.numero_nodi = numero_nodi   # Total number of vertices in the graph
        self.graph = []     # Array of edges

    def insert(self, nodo_sorgente, nodo_destinazione, peso):
        self.graph.append([nodo_sorgente, nodo_destinazione, peso])

    def distanza(self, distance):  # print the distance from the source considered
        for nodo in range(self.numero_nodi):
            print("{0}\t\t{1}".format(nodo, distance[nodo]))

    def Bellman_Ford(self, source_node):
        """
        implementation of the Bellman-Ford algorithm for the shortest path from a single source vertex
        :param source_node: source vertex
        :return: vertex distance from source
        """
        distance = [float("Inf")] * self.numero_nodi
        distance[source_node] = 0

        for _ in range(self.numero_nodi - 1):  # relax edges |V| - 1 times
            for n_partenza, n_destinazione, peso in self.graph:
                if distance[n_partenza] != float("Inf") and distance[n_partenza] + peso < distance[n_destinazione]:
                    distance[n_destinazione] = distance[n_partenza] + peso

        for n_partenza, n_destinazione, peso in self.graph:  # if there are negative cycle --> HUGE PROBLEM!
            if distance[n_partenza] != float("Inf") and distance[n_partenza] + peso < distance[n_destinazione]:
                print("iL GRAFO CONTIENE CICLI NEGATIVI E L'ALGORITMO... NON FUNZIONA!")
                return

        return self.distanza(distance)


g = Graph_BF(5)
g.insert(0, 1, 12)
g.insert(0, 2, 4)
g.insert(1, 3, 3)
g.insert(2, 1, 6)
g.insert(3, 2, 2)

g.Bellman_Ford(0)