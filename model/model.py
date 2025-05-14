import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._listProducts = None
        self.anno = None
        self.color = None
        self._graph = nx.Graph()
        self._nodes = []
        self._idMap = {}



    def getAnno(self):
        self.anno = DAO.get_anno()
        return self.anno

    def getColors(self):
        self.color = DAO.get_colors()
        return self.color

    def loadProducts(self):
        self._listProducts = DAO.getAllProducts()

    @property
    def listProducts(self):
        return self._listProducts

    def buildGraph(self, c, a):
        self._graph.clear()
        for p in self._listProducts:
            if p.Product_color == c:
                self._nodes.append(p)

        self._graph.add_nodes_from(self._nodes)
        self._idMap = {}

        for n in self._nodes:
            self._idMap[n.Product_number] = n




    def addEdges(self):
        pass

    def getNumNodes(self):
        return len(self._graph.nodes)

    def getNumEdges(self):
        return len(self._graph.edges)

    def getNodes(self):
        return self._graph.nodes()
