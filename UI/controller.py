import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listColor = []

    def fillDD(self):
        self._listYear = self._model.getAnno()
        for i in self._listYear:
            self._view._ddyear.options.append(ft.dropdown.Option(i))
        self._view.update_page()

        self._listColor = self._model.getColors()
        for i in self._listColor:
            self._view._ddcolor.options.append(ft.dropdown.Option(i))
        self._view.update_page()


    def handle_graph(self, e):
        a = self._view._ddyear.value
        c = self._view._ddcolor.value

        self._model.loadProducts()
        self._model.buildGraph(c,a)

        self.fillDDProduct()

        self._view.txtOut.controls.clear()
        self._view.txtOut.controls.append(ft.Text(f"Numero di vertici: {self._model.getNumNodes()}  Numero di archi: {self._model.getNumEdges}"))

        self._view.update_page()



    def fillDDProduct(self):
        for n in self._model.getNodes():
            pass


    def handle_search(self, e):
        pass


