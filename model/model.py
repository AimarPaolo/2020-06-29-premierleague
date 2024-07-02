import copy

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self.nodi = []
        self.idMap = {}
        self.listaMax = []
        self.pesoMax = None

    def buildGraph(self, mese, minuti):
        self._grafo.clear()
        self.nodi = DAO.getNodes(mese)
        self._grafo.add_nodes_from(self.nodi)
        for f in self.nodi:
            self.idMap[f.MatchID] = f
        self.addEdges(mese, minuti)

    def addEdges(self, mese, minuti):
        self._grafo.clear_edges()
        for match1, match2, peso in DAO.nome2(mese, minuti):
            n1 = self.idMap[match1]
            n2 = self.idMap[match2]
            if match1 != match2:
                if peso > 0:
                    if self._grafo.has_edge(n1, n2) is False:
                        self._grafo.add_edge(n1, n2, weight=peso)
                        if self.pesoMax is None:
                            self.pesoMax = peso
                            self.listaMax = [(n1, n2, peso)]
                        else:
                            if self.pesoMax == peso:
                                self.listaMax.append((n1, n2))
                            elif self.pesoMax < peso:
                                self.listaMax = [(n1, n2)]
                                self.pesoMax = peso

    def getPesoMax(self):
        return self.pesoMax, self.listaMax

    def ricorsione(self, parziale, v0):
        if v0 in parziale:
            if self.peso(parziale) > self._costBest:
                self._costBest = self.peso(parziale)
                self._solBest = copy.deepcopy(parziale)

        for v in self._grafo.nodes:
            if v not in self._grafo.neighbors(parziale[-1]):
                if v not in parziale:
                    parziale.append(v)
                    self.ricorsione(parziale, v0)
                    parziale.pop()

    def peso(self, parziale):
        peso = 0
        for nodi in parziale:
            peso += nodi.condiment_calories
        return peso

    def getCaratteristiche(self):
        return len(self._grafo.nodes), len(self._grafo.edges)