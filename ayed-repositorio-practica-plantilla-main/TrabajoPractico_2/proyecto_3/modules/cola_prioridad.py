from Monticulo import MonticuloBinario

class ColaPrioridad:
    def __init__(self):
        self.monticulo = MonticuloBinario()
        self.prioridades = {}  # Para llevar control de la menor prioridad conocida de cada nodo

    def encolar(self, prioridad, nodo):
        if nodo not in self.prioridades or prioridad < self.prioridades[nodo]:
            self.prioridades[nodo] = prioridad
            self.monticulo.insertar((prioridad, nodo))

    def desencolar(self):
        while True:
            if self.monticulo.tamanoActual == 0:
                return None, None
            prioridad, nodo = self.monticulo.eliminarMin()
            if self.prioridades.get(nodo) == prioridad:
                return prioridad, nodo

    def esta_vacia(self):
        return self.monticulo.tamanoActual == 0
