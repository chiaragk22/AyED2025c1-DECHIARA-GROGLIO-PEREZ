from nodos import Nodo

class ListaDobleEnlazada:
    def __init__ (self):
        self.cabeza = None
        self.cola = None
        self.tamanio = 0


    def esta_vacia(self):
        return self.cabeza == None
    
    def __len__(self):
        
        return self.tamanio
    
    def agregar_al_inicio(self, item):
        Nodo_nuevo = Nodo(item)
        if self.cabeza is not None:
            self.cabeza.asignarAnterior(Nodo_nuevo)
            Nodo_nuevo.asignarSiguiente(self.cabeza)
            self.cabeza = Nodo_nuevo
        else:
            self.cabeza = Nodo_nuevo
            self.cola = Nodo_nuevo
            # self.cola.asignarSiguiente(None)
            # self.cabeza.asignarAnterior(None)
        
        self.tamanio += 1


    def agregar_al_final(self,item):
        Nodo_nuevo = Nodo(item)
        if self.cabeza == None:
            self.cabeza = Nodo_nuevo
            self.cola = Nodo_nuevo
            # self.cola.asignarSiguiente(None)
            # self.cabeza.asignarAnterior(None)
        else:
            self.cola.asignarSiguiente(Nodo_nuevo)
            Nodo_nuevo.asignarAnterior(self.cola)
            self.cola = Nodo_nuevo
            # self.cola.asignarSiguiente(None)
        self.tamanio += 1    
        
    
    def insertar(self,item,posicion):
        Nodo_nuevo = Nodo(item)
        if posicion < 0 or posicion > self.tamanio:
            raise IndexError("Posición fuera de rango")

        elif posicion ==  None or posicion == self.tamanio - 1:
            self.agregar_al_final(item)
            self.tamanio += 1   
            return
        
        elif posicion == 0:
            self.agregar_al_inicio(item)
            self.tamanio += 1
            return

        else:
            actual = self.cabeza
            for i in range(posicion):
                actual = actual.obtenerSiguiente()

            Nodo_nuevo.asignarSiguiente(actual)
            Nodo_nuevo.asignarAnterior(actual.obtenerAnterior())
            actual.asignarAnterior(Nodo_nuevo)
            actual.obtenerAnterior().asignarSiguiente(Nodo_nuevo)
            
            self.tamanio += 1

    def extraer(self, posicion):

        if self.cabeza is None:
            raise IndexError("La lista está vacía")
        
        elif posicion < 0 or posicion > self.tamanio:
            raise IndexError("Posición fuera de rango")
        
        elif posicion == None or posicion == self.tamanio - 1:
            # self.cola.obtenerAnterior().asignarSiguiente(None)
            cola_original = self.cola
            self.cola = self.cola.obtenerAnterior()
            self.tamanio -= 1
            return cola_original
        
        elif posicion == 0:
                # self.cabeza.obtenerSiguiente().asignarAnterior(None)
                cabeza_original = self.cabeza
                self.cabeza = self.cabeza.obtenerSiguiente()    
                self.tamanio -= 1
                return cabeza_original
            
        else:
            actual = self.cabeza
            for i in range(posicion):
                actual = actual.obtenerSiguiente()
 
            actual.obtenerAnterior().asignarSiguiente(actual.obtenerSiguiente())
            actual.obtenerSiguiente().asignarAnterior(actual.obtenerAnterior())
            self.tamanio -= 1
            return actual.obtenerDato()
            
    
    def copiar(self):
        if self.cabeza is None:
            return ListaDobleEnlazada(None)

        nueva_lista = ListaDobleEnlazada(None)
        actual_original = self.cabeza

        nueva_cabeza = Nodo(actual_original.obtenerDato())
        nueva_lista.cabeza = nueva_cabeza
        nuevo_actual = nueva_cabeza
        actual_original = actual_original.obtenerSiguiente()

        while actual_original is not None:
            nuevo_nodo = Nodo(actual_original.obtenerDato())
            nuevo_actual.asignarSiguiente(nuevo_nodo)
            nuevo_nodo.asignarAnterior(nuevo_actual)

            nuevo_actual = nuevo_nodo
            actual_original = actual_original.obtenerSiguiente()
            
        
        nueva_lista.cola = nuevo_actual 

        return nueva_lista
    
    def invertir(self):
        if self.cabeza is None:
            return

        actual = self.cabeza
        anterior = None

        while actual is not None:
            siguiente = actual.obtenerSiguiente()
            actual.asignarSiguiente(anterior)
            actual.asignarAnterior(siguiente)
            anterior = actual
            actual = siguiente

        self.cabeza = anterior
        
    def invert(self):
        nueva_lista = ListaDobleEnlazada()
        for i in range(self.tamanio)-1:
            nueva_lista.cabeza = self.cola.obtenerDato()
            
    def mostrarlista(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.obtenerDato())
            actual = actual.obtenerSiguiente()
            
if __name__ == "__main__":
    lista = ListaDobleEnlazada()
    lista.agregar_al_inicio(1)
    lista.agregar_al_final(2)
    lista.agregar_al_final(3)
    lista.agregar_al_final(4)
    lista.agregar_al_final(5)
    lista.mostrarlista()
    print("Tamaño de la lista:", len(lista))
    print("Elemento extraído:", lista.extraer(2))
    lista.mostrarlista()
    print("Tamaño de la lista después de extraer:", len(lista))
    lista.invertir()
    lista.mostrarlista()
            