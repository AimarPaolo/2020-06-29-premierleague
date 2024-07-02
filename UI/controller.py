import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listCountry = []

    def fillDDmese(self):
        mesi = ["Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno", "Luglio", "Agosto", "Settembre", "Ottobre", "Novembre", "Dicemebre"]
        for i in range(12):
            self._view.ddmese.options.append(ft.dropdown.Option(text=f"{mesi[i]}", key=f"{i+1}"))

    def fillM1(self):
        for i in self._model._grafo.nodes:
            self._view.ddm1.options.append(ft.dropdown.Option(data=i, text=f"{i.MatchID}"))

    def fillM2(self):
        pass

    def handle_graph(self, e):
        self._view.txt_result.controls.clear()
        min_str = self._view.txt_min.value
        try:
            minuti = int(min_str)
        except ValueError:
            self._view.txt_result.controls.append(ft.Text(f"Errore nell'inserimento dei minuti!!"))
            self._view.update_page()
            return
        mese = self._view.ddmese.value
        if mese is None:
            self._view.txt_result.controls.append(ft.Text(f"Selezionare un mese!!"))
            self._view.update_page()
            return
        self._model.buildGraph(mese, minuti)
        self._view.txt_result.controls.append(ft.Text(f"Grafo correttamente creato!"))
        nNodes, nEdges = self._model.getCaratteristiche()
        self._view.txt_result.controls.append(ft.Text(f"Il grafo creato ha {nNodes} nodi"))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo creato ha {nEdges} archi"))
        self._view.update_page()

    def handle_connesione_max(self, e):
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Coppie con connessione massima"))
        peso, lista = self._model.getPesoMax()
        for m1, m2 in lista:
            self._view.txt_result.controls.append(ft.Text(f"[{m1.MatchID}] nomi dei team presi con DAO o altri metodi - [{m2.MatchID}] ({peso})"))
        self._view.update_page()

    def handle_collegamento(self, e):
        pass
