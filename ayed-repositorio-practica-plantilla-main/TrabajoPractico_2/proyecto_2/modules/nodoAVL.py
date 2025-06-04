class NodoAVL:
    def __init__(self, fecha, temperatura):
        self.fecha = fecha                   # tipo datetime 
        self.temperatura = temperatura       # tipo float 
        self.altura = 1                      # altura del nodo en el árbol
        self.izquierda = None
        self.derecha = None
