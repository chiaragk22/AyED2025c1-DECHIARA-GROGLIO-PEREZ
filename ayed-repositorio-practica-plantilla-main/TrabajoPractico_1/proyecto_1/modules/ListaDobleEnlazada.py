from nodos import Nodo

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
    
    def agregar_al_inicio(self, item):
        Nodo_nuevo = Nodo(item)
        Nodo_nuevo.asignarSiguiente(self.cabeza)
        if self.cabeza is not None:
            self.cabeza.asignarAnterior(Nodo_nuevo)
        self.cabeza = Nodo_nuevo


    def agregar_al_final(self,item):
        Nodo_nuevo = Nodo(item)
        if self.cabeza == None:
            self.cabeza = Nodo_nuevo
        else:
            actual = self.cabeza
            while actual.obtenerSiguiente() != None:
                actual = actual.obtenerSiguiente()
            actual.asignarSiguiente(Nodo_nuevo)
            Nodo_nuevo.asignarAnterior(actual)
        
    
    def insertar(self,item,posicion):
        Nodo_nuevo = Nodo(item)

        if posicion ==  None:
            self.agregar_al_final(item)
            return
        else:
            for i in range(posicion):
                if i == 0:
                    Nodo_nuevo.asignarSiguiente(self.cabeza)
                    if self.cabeza is not None:
                        self.cabeza.asignarAnterior(Nodo_nuevo)
                    self.cabeza = Nodo_nuevo
                    return
               
                else:
                    actual = self.cabeza
                    indice = 1
                    while actual is not None and indice < posicion:
                        actual = actual.obtenerSiguiente()
                        indice += 1

                    if actual is None:
                        raise IndexError("Posición fuera de rango")

  
                    Nodo_nuevo.asignarSiguiente(actual.obtenerSiguiente())
                    Nodo_nuevo.asignarAnterior(actual)
                    if actual.obtenerSiguiente() is not None:
                        actual.obtenerSiguiente().asignarAnterior(Nodo_nuevo)
                    actual.asignarSiguiente(Nodo_nuevo)

    def extraer(self, posicion):

        if self.cabeza is None:
            raise IndexError("La lista está vacía")
        
        if posicion == None:
            actual = self.cabeza
            while actual.obtenerSiguiente() is not None:
                actual = actual.obtenerSiguiente()

            actual.obtenerAnterior().asignarSiguiente(None)
            return actual.obtenerDato()
        
        else:
            actual = self.cabeza
            for i in range(posicion):
                if actual is None:
                    raise IndexError("Posición fuera de rango")
                actual = actual.obtenerSiguiente()
            
            if actual is None:
                raise IndexError("Posición fuera de rango")
            
            if actual.obtenerAnterior() is not None:
                actual.obtenerAnterior().asignarSiguiente(actual.obtenerSiguiente())
            else:
                self.cabeza = actual.obtenerSiguiente()
            
            if actual.obtenerSiguiente() is not None:
                actual.obtenerSiguiente().asignarAnterior(actual.obtenerAnterior())
            else:
                actual.obtenerAnterior().asignarSiguiente(None)

        return actual.obtenerDato()