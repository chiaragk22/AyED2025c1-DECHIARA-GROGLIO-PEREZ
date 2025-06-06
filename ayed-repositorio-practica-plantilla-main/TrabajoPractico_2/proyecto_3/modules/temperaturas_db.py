# TP2_TemperaturasDB/temperaturas_db.py

from datetime import datetime
from modules.avl import AVLTree

class Temperaturas_DB:
    """
    Base de datos en memoria para temperaturas, usando un árbol AVL genérico (avl.AVLTree).
    Clave interna: datetime.date
    Valor interno: float

    Métodos:
      - guardar_temperatura(temp, fecha_str)
      - devolver_temperatura(fecha_str)
      - borrar_temperatura(fecha_str)
      - cantidad_muestras()
      - devolver_temperaturas(fecha1_str, fecha2_str)
      - max_temp_rango(fecha1_str, fecha2_str)
      - min_temp_rango(fecha1_str, fecha2_str)
      - temp_extremos_rango(fecha1_str, fecha2_str)
    """

    def __init__(self):
        # Instanciamos un AVLTree vacío
        self._arbol = AVLTree()

    def _parsear_fecha(self, fecha_str):
        """
        Convierte cadena "dd/mm/aaaa" a datetime.date.
        En caso de formato inválido, lanza ValueError.
        """
        return datetime.strptime(fecha_str, "%d/%m/%Y").date()

    def guardar_temperatura(self, temperatura, fecha_str):
        """
        Inserta o actualiza temperatura (float) para la fecha dada.
        Delegamos en AVLTree.insertar(clave, valor).
        Complejidad promedio: O(log n).
        """
        fecha = self._parsear_fecha(fecha_str)
        self._arbol.insertar(fecha, float(temperatura))

    def devolver_temperatura(self, fecha_str):
        """
        Busca la temperatura en la fecha dada. 
        Retorna float o None si no existe.
        Complejidad: O(log n).
        """
        fecha = self._parsear_fecha(fecha_str)
        nodo = self._arbol.buscar(fecha)
        return nodo.valor if nodo else None

    def borrar_temperatura(self, fecha_str):
        """
        Elimina el registro de la fecha indicada.
        Si no existe, no hace nada.
        Complejidad: O(log n).
        """
        fecha = self._parsear_fecha(fecha_str)
        self._arbol.eliminar(fecha)

    def cantidad_muestras(self):
        """
        Devuelve la cantidad total de nodos (fechas) en el AVL.
        Implementación sencilla: recorre todo el árbol (O(n)).
        """
        def _contar(nodo):
            if nodo is None:
                return 0
            return 1 + _contar(nodo.izquierdo) + _contar(nodo.derecho)

        return _contar(self._arbol._raiz)

    def devolver_temperaturas(self, fecha1_str, fecha2_str):
        """
        Retorna lista de cadenas "dd/mm/aaaa: XX.X °C" para todas las fechas
        entre fecha1 y fecha2 inclusive, ordenadas de menor a mayor fecha.
        Complejidad: O(k + log n), k = nodos en el rango.
        """
        f1 = self._parsear_fecha(fecha1_str)
        f2 = self._parsear_fecha(fecha2_str)
        if f2 < f1:
            f1, f2 = f2, f1

        lista_nodos = self._arbol.recorrido_en_rango(f1, f2)
        resultado = []
        for nodo in lista_nodos:
            fecha_c = nodo.clave.strftime("%d/%m/%Y")
            resultado.append(f"{fecha_c}: {nodo.valor} °C")
        return resultado

    def max_temp_rango(self, fecha1_str, fecha2_str):
        """
        Retorna la temperatura máxima (float) en [fecha1, fecha2]. 
        Si no hay datos, devuelve None.
        Complejidad: O(k + log n).
        """
        f1 = self._parsear_fecha(fecha1_str)
        f2 = self._parsear_fecha(fecha2_str)
        if f2 < f1:
            f1, f2 = f2, f1

        nodos = self._arbol.recorrido_en_rango(f1, f2)
        if not nodos:
            return None

        maxima = nodos[0].valor
        for nd in nodos:
            if nd.valor > maxima:
                maxima = nd.valor
        return maxima

    def min_temp_rango(self, fecha1_str, fecha2_str):
        """
        Retorna la temperatura mínima (float) en [fecha1, fecha2]. 
        Si no hay datos, devuelve None.
        Complejidad: O(k + log n).
        """
        f1 = self._parsear_fecha(fecha1_str)
        f2 = self._parsear_fecha(fecha2_str)
        if f2 < f1:
            f1, f2 = f2, f1

        nodos = self._arbol.recorrido_en_rango(f1, f2)
        if not nodos:
            return None

        minima = nodos[0].valor
        for nd in nodos:
            if nd.valor < minima:
                minima = nd.valor
        return minima

    def temp_extremos_rango(self, fecha1_str, fecha2_str):
        """
        Retorna tupla (min, max) de temperaturas en [fecha1, fecha2].
        Si no hay datos, devuelve (None, None).
        Complejidad: O(k + log n).
        """
        t_min = self.min_temp_rango(fecha1_str, fecha2_str)
        t_max = self.max_temp_rango(fecha1_str, fecha2_str)
        return (t_min, t_max)
