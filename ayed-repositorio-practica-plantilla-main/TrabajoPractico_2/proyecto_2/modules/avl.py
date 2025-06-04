# TP2_TemperaturasDB/avl.py


class NodoAVL:
    """
    Nodo genérico del árbol AVL.
    Cada nodo almacena:
      - clave: puede ser cualquier tipo comparable (aquí usaremos datetime.date).
      - valor: el dato asociado a la clave (float en el caso de temperaturas).
      - altura: altura del subárbol para balanceo.
      - izquierdo, derecho: referencias a subárboles.
    """
    def __init__(self, clave, valor):
        self.clave = clave        # por ejemplo, datetime.date
        self.valor = valor        # por ejemplo, float
        self.altura = 1
        self.izquierdo = None
        self.derecho = None

def _altura(nodo):
    """Devuelve la altura de un nodo (0 si es None)."""
    return nodo.altura if nodo else 0

def _actualizar_altura(nodo):
    """Recálcula la altura de 'nodo' según sus hijos."""
    nodo.altura = 1 + max(_altura(nodo.izquierdo), _altura(nodo.derecho))

def _factor_balance(nodo):
    """Retorna la diferencia (altura izquierda – altura derecha)."""
    return _altura(nodo.izquierdo) - _altura(nodo.derecho) if nodo else 0

def _rotacion_derecha(z):
    """
    Rotación simple a la derecha en z:
      - x = z.izquierdo
      - z.izquierdo = x.derecho
      - x.derecho = z
      - actualizar alturas y devolver x como nueva raíz
    """
    x = z.izquierdo
    T2 = x.derecho

    x.derecho = z
    z.izquierdo = T2

    _actualizar_altura(z)
    _actualizar_altura(x)
    return x

def _rotacion_izquierda(z):
    """
    Rotación simple a la izquierda en z:
      - y = z.derecho
      - z.derecho = y.izquierdo
      - y.izquierdo = z
      - actualizar alturas y devolver y como nueva raíz
    """
    y = z.derecho
    T2 = y.izquierdo

    y.izquierdo = z
    z.derecho = T2

    _actualizar_altura(z)
    _actualizar_altura(y)
    return y

class AVLTree:
    """
    Clase pública para manejar un árbol AVL genérico.
    Soporta:
      - insertar(clave, valor)
      - buscar(clave) → devuelve nodo o None
      - eliminar(clave)
      - recorrido_en_rango(fecha1, fecha2) → lista de nodos en rango
    """

    def __init__(self):
        self._raiz = None

    def insertar(self, clave, valor):
        """
        Inserta (clave, valor) en el árbol. Si la clave existe, sobrescribe el valor.
        Complejidad promedio: O(log n).
        """
        self._raiz = self._insertar_nodo(self._raiz, clave, valor)

    def _insertar_nodo(self, nodo, clave, valor):
        if nodo is None:
            return NodoAVL(clave, valor)

        if clave < nodo.clave:
            nodo.izquierdo = self._insertar_nodo(nodo.izquierdo, clave, valor)
        elif clave > nodo.clave:
            nodo.derecho = self._insertar_nodo(nodo.derecho, clave, valor)
        else:
            # Ya existía la clave: actualizamos el valor y no creamos nodo nuevo.
            nodo.valor = valor
            return nodo

        _actualizar_altura(nodo)
        fb = _factor_balance(nodo)

        # Caso LL
        if fb > 1 and clave < nodo.izquierdo.clave:
            return _rotacion_derecha(nodo)
        # Caso RR
        if fb < -1 and clave > nodo.derecho.clave:
            return _rotacion_izquierda(nodo)
        # Caso LR
        if fb > 1 and clave > nodo.izquierdo.clave:
            nodo.izquierdo = _rotacion_izquierda(nodo.izquierdo)
            return _rotacion_derecha(nodo)
        # Caso RL
        if fb < -1 and clave < nodo.derecho.clave:
            nodo.derecho = _rotacion_derecha(nodo.derecho)
            return _rotacion_izquierda(nodo)

        return nodo

    def buscar(self, clave):
        """
        Busca un nodo con la clave dada. Devuelve el nodo o None.
        Complejidad promedio: O(log n).
        """
        return self._buscar_nodo(self._raiz, clave)

    def _buscar_nodo(self, nodo, clave):
        if nodo is None:
            return None
        if clave < nodo.clave:
            return self._buscar_nodo(nodo.izquierdo, clave)
        elif clave > nodo.clave:
            return self._buscar_nodo(nodo.derecho, clave)
        else:
            return nodo

    def eliminar(self, clave):
        """
        Elimina el nodo con la clave dada (si existe). Complejidad: O(log n).
        """
        self._raiz = self._eliminar_nodo(self._raiz, clave)

    def _encontrar_min(self, nodo):
        """Devuelve el nodo con la clave mínima en el subárbol."""
        actual = nodo
        while actual.izquierdo is not None:
            actual = actual.izquierdo
        return actual

    def _eliminar_nodo(self, nodo, clave):
        if nodo is None:
            return None

        if clave < nodo.clave:
            nodo.izquierdo = self._eliminar_nodo(nodo.izquierdo, clave)
        elif clave > nodo.clave:
            nodo.derecho = self._eliminar_nodo(nodo.derecho, clave)
        else:
            # Nodo a borrar encontrado
            if nodo.izquierdo is None:
                return nodo.derecho
            elif nodo.derecho is None:
                return nodo.izquierdo

            # Dos hijos: reemplazar con sucesor in‐order
            temp = self._encontrar_min(nodo.derecho)
            nodo.clave = temp.clave
            nodo.valor = temp.valor
            nodo.derecho = self._eliminar_nodo(nodo.derecho, temp.clave)

        if nodo is None:
            return None

        _actualizar_altura(nodo)
        fb = _factor_balance(nodo)

        # Caso LL
        if fb > 1 and _factor_balance(nodo.izquierdo) >= 0:
            return _rotacion_derecha(nodo)
        # Caso LR
        if fb > 1 and _factor_balance(nodo.izquierdo) < 0:
            nodo.izquierdo = _rotacion_izquierda(nodo.izquierdo)
            return _rotacion_derecha(nodo)
        # Caso RR
        if fb < -1 and _factor_balance(nodo.derecho) <= 0:
            return _rotacion_izquierda(nodo)
        # Caso RL
        if fb < -1 and _factor_balance(nodo.derecho) > 0:
            nodo.derecho = _rotacion_derecha(nodo.derecho)
            return _rotacion_izquierda(nodo)

        return nodo

    def recorrido_en_rango(self, clave1, clave2):
        """
        Retorna una lista de nodos cuyo atributo .clave está entre [clave1, clave2] inclusive,
        en orden creciente de clave. Complejidad: O(k + log n), donde k=nods en rango.
        """
        lista = []
        self._recorrer_rango(self._raiz, clave1, clave2, lista)
        return lista

    def _recorrer_rango(self, nodo, clave1, clave2, lista):
        if nodo is None:
            return
        if clave1 < nodo.clave:
            self._recorrer_rango(nodo.izquierdo, clave1, clave2, lista)
        if clave1 <= nodo.clave <= clave2:
            lista.append(nodo)
        if nodo.clave < clave2:
            self._recorrer_rango(nodo.derecho, clave1, clave2, lista)
