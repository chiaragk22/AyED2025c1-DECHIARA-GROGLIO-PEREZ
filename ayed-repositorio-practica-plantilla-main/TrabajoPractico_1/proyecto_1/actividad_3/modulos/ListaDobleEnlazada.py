from modulos.nodos import Nodo

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
        if self.cabeza is None:
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
        
    
    def insertar(self,item,posicion = None):
        Nodo_nuevo = Nodo(item)
        if posicion < 0 or posicion > self.tamanio:
            raise IndexError("Posición fuera de rango")

        elif posicion is None or posicion == self.tamanio:
            self.agregar_al_final(item)
              
            return
        
        elif posicion == 0:
            self.agregar_al_inicio(item)
            
            return

        else:
            actual = self.cabeza
            for i in range(posicion):
                actual = actual.obtenerSiguiente()

            Nodo_nuevo.asignarSiguiente(actual)
            Nodo_nuevo.asignarAnterior(actual.obtenerAnterior())
            if actual.obtenerAnterior() is not None:
                actual.obtenerAnterior().asignarSiguiente(Nodo_nuevo)

            actual.asignarAnterior(Nodo_nuevo)
            
            
            self.tamanio += 1

    def extraer(self, posicion=None):

        if self.cabeza is None:
            raise IndexError("La lista está vacía")
        
        if posicion is None:
            posicion = self.tamanio -1
        
        if posicion < 0:
            posicion += self.tamanio
        
        if posicion < 0 or posicion > self.tamanio:
            raise IndexError("Posición fuera de rango")
        
        elif posicion == self.tamanio-1:
            cola_original = self.cola
            dato_cola_original = cola_original.obtenerDato()
            self.cola = self.cola.obtenerAnterior()
            if self.cola is not None:
                self.cola.asignarSiguiente(None)  
            else:
                self.cabeza = None  
            self.tamanio -= 1
            
            return dato_cola_original
        
        elif posicion == 0:
                cabeza_original = self.cabeza
                dato_cab_original = cabeza_original.obtenerDato()
                self.cabeza = self.cabeza.obtenerSiguiente()    
                if self.cabeza is not None:
                    self.cabeza.asignarAnterior(None)  
                else:
                    self.cola = None  
                self.tamanio -= 1
                return dato_cab_original
                
        else:
            actual = self.cabeza
            for i in range(posicion):
                actual = actual.obtenerSiguiente()
 
            actual.obtenerAnterior().asignarSiguiente(actual.obtenerSiguiente())
            if actual.obtenerSiguiente() is not None:
                actual.obtenerSiguiente().asignarAnterior(actual.obtenerAnterior())
            self.tamanio -= 1
            return actual.obtenerDato()
            
    
    def copiar(self):
        if self.cabeza is None:
            return ListaDobleEnlazada()

        nueva_lista = ListaDobleEnlazada()
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
        nueva_lista.tamanio = self.tamanio

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

        self.cola = self.cabeza
        self.cabeza = anterior
        
            
    def mostrarlista(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.obtenerDato())
            actual = actual.obtenerSiguiente()

    def __iter__(self):
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            yield nodo_actual.obtenerDato()
            nodo_actual = nodo_actual.obtenerSiguiente()
            

    def concatenar(self, nueva_lista):
        otra_lista = nueva_lista.copiar()  # Copia la otra lista para evitar modificarla
        if otra_lista.cabeza is None:
            return  # Si la otra lista está vacía, no hay nada que concatenar

        if self.cabeza is None:
            # Si la lista actual está vacía, simplemente asignamos la otra lista
            self.cabeza = otra_lista.cabeza
            self.cola = otra_lista.cola
        else:
            # Conectar la cola de la lista actual con la cabeza de la otra lista
            self.cola.asignarSiguiente(otra_lista.cabeza)
            otra_lista.cabeza.asignarAnterior(self.cola)
            self.cola = otra_lista.cola

        # Asegurar que el puntero siguiente de la nueva cola sea None
        if self.cola is not None:
            self.cola.asignarSiguiente(None)

        # Actualizar el tamaño de la lista
        self.tamanio += otra_lista.tamanio

    def __add__(self, otra_lista):
        nueva_lista = self.copiar()
        nueva_lista.concatenar(otra_lista)
            
        # Asegurar que los punteros cabeza y cola estén correctamente configurados
        if nueva_lista.cabeza is not None:
            nueva_lista.cabeza.asignarAnterior(None)
        if nueva_lista.cola is not None:
            nueva_lista.cola.asignarSiguiente(None)

        return nueva_lista  # Devolver la nueva lista resultante
    
    
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
    
