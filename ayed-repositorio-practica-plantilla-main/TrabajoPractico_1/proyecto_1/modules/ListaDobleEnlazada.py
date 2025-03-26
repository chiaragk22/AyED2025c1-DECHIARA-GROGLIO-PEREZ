class ListaDobleEnlazada:
    def __init__ (self,datoinicial):
        self.cabeza = None


    def esta_vacia(self):
        return self.cabeza == None
    
    def __len__(self):
        actual = self.cabeza
        contador = 0
        while actual != None:
            contador = contador + 1
            actual = actual.obtenerSiguiente()

        return contador
    

    def agregar_al_inicio(self,item):
        temp = Nodo(item)
        temp.asignarSiguiente(self.cabeza)
        self.cabeza = temp