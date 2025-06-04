from datetime import datetime
from modules.nodoAVL import NodoAVL

class Temperaturas_DB:
    def __init__(self):
        self.raiz = None
        self._cantidad = 0

    def guardar_temperatura(self, temperatura, fecha_str):
        fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
        self.raiz = self._insertar(self.raiz, fecha, temperatura)

    def devolver_temperatura(self, fecha_str):
        fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
        nodo = self._buscar(self.raiz, fecha)
        return nodo.temperatura if nodo else None

    def borrar_temperatura(self, fecha_str):
        fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
        self.raiz = self._eliminar(self.raiz, fecha)

    def cantidad_muestras(self):
        return self._cantidad

    def max_temp_rango(self, f1, f2):
        fechas = self._filtrar_rango(self.raiz, self._parse_fecha(f1), self._parse_fecha(f2))
        return max(f.temperatura for f in fechas) if fechas else None

    def min_temp_rango(self, f1, f2):
        fechas = self._filtrar_rango(self.raiz, self._parse_fecha(f1), self._parse_fecha(f2))
        return min(f.temperatura for f in fechas) if fechas else None

    def temp_extremos_rango(self, f1, f2):
        fechas = self._filtrar_rango(self.raiz, self._parse_fecha(f1), self._parse_fecha(f2))
        if not fechas:
            return None, None
        temps = [f.temperatura for f in fechas]
        return min(temps), max(temps)

    def devolver_temperaturas(self, f1, f2):
        fechas = self._filtrar_rango(self.raiz, self._parse_fecha(f1), self._parse_fecha(f2))
        fechas.sort(key=lambda nodo: nodo.fecha)
        return [f"{nodo.fecha.strftime('%d/%m/%Y')}: {nodo.temperatura} ºC" for nodo in fechas]

    # --- Funciones internas ---

    def _parse_fecha(self, fecha_str):
        return datetime.strptime(fecha_str, "%d/%m/%Y")

    def _insertar(self, nodo, fecha, temperatura):
        if not nodo:
            self._cantidad += 1
            return NodoAVL(fecha, temperatura)
        elif fecha < nodo.fecha:
            nodo.izquierda = self._insertar(nodo.izquierda, fecha, temperatura)
        elif fecha > nodo.fecha:
            nodo.derecha = self._insertar(nodo.derecha, fecha, temperatura)
        else:  # actualizar si ya existe
            nodo.temperatura = temperatura
            return nodo

        nodo.altura = 1 + max(self._altura(nodo.izquierda), self._altura(nodo.derecha))
        return self._balancear(nodo)

    def _buscar(self, nodo, fecha):
        if not nodo:
            return None
        if fecha < nodo.fecha:
            return self._buscar(nodo.izquierda, fecha)
        elif fecha > nodo.fecha:
            return self._buscar(nodo.derecha, fecha)
        else:
            return nodo

    def _eliminar(self, nodo, fecha):
        if not nodo:
            return None
        if fecha < nodo.fecha:
            nodo.izquierda = self._eliminar(nodo.izquierda, fecha)
        elif fecha > nodo.fecha:
            nodo.derecha = self._eliminar(nodo.derecha, fecha)
        else:
            self._cantidad -= 1
            if not nodo.izquierda:
                return nodo.derecha
            elif not nodo.derecha:
                return nodo.izquierda
            temp = self._min_nodo(nodo.derecha)
            nodo.fecha, nodo.temperatura = temp.fecha, temp.temperatura
            nodo.derecha = self._eliminar(nodo.derecha, temp.fecha)

        nodo.altura = 1 + max(self._altura(nodo.izquierda), self._altura(nodo.derecha))
        return self._balancear(nodo)

    def _filtrar_rango(self, nodo, f1, f2):
        if not nodo:
            return []
        resultado = []
        if f1 <= nodo.fecha <= f2:
            resultado.append(nodo)
        if nodo.fecha > f1:
            resultado += self._filtrar_rango(nodo.izquierda, f1, f2)
        if nodo.fecha < f2:
            resultado += self._filtrar_rango(nodo.derecha, f1, f2)
        return resultado

    def _altura(self, nodo):
        return nodo.altura if nodo else 0

    def _balance_factor(self, nodo):
        return self._altura(nodo.izquierda) - self._altura(nodo.derecha)

    def _balancear(self, nodo):
        balance = self._balance_factor(nodo)

        if balance > 1:
            if self._balance_factor(nodo.izquierda) < 0:
                nodo.izquierda = self._rotar_izq(nodo.izquierda)
            return self._rotar_der(nodo)

        if balance < -1:
            if self._balance_factor(nodo.derecha) > 0:
                nodo.derecha = self._rotar_der(nodo.derecha)
            return self._rotar_izq(nodo)

        return nodo

    def _rotar_der(self, y):
        x = y.izquierda
        T2 = x.derecha
        x.derecha = y
        y.izquierda = T2
        y.altura = 1 + max(self._altura(y.izquierda), self._altura(y.derecha))
        x.altura = 1 + max(self._altura(x.izquierda), self._altura(x.derecha))
        return x

    def _rotar_izq(self, x):
        y = x.derecha
        T2 = y.izquierda
        y.izquierda = x
        x.derecha = T2
        x.altura = 1 + max(self._altura(x.izquierda), self._altura(x.derecha))
        y.altura = 1 + max(self._altura(y.izquierda), self._altura(y.derecha))
        return y

    def _min_nodo(self, nodo):
        actual = nodo
        while actual.izquierda:
            actual = actual.izquierda
        return actual
