from modules.Monticulo import MonticuloBinario

class ColaPrioridad:
    def __init__(self):
        self.monticulo = MonticuloBinario()

    def encolar(self, elemento):
        self.monticulo.insertar(elemento)

    def desencolar(self):
        return self.monticulo.eliminarMin()

    def esta_vacia(self):
        return self.monticulo.tamanoActual == 0

    def __iter__(self):
        for elemento in self.monticulo.listaMonticulo[1:]:
            yield elemento

    def __len__(self):
        return self.monticulo.tamanoActual

