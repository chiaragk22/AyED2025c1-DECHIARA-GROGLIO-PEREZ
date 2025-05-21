# mazo.py

from modulos.ListaDobleEnlazada import ListaDobleEnlazada


class DequeEmptyError(Exception):
    pass  

class Mazo:
    def __init__(self):
        self.cartas = ListaDobleEnlazada()

    def esta_vacio(self):
        return len(self.cartas) == 0

    def poner_carta_abajo(self, carta):
        self.cartas.agregar_al_final(carta)

    def sacar_carta_arriba(self, mostrar=False):
        if self.esta_vacio():
            raise DequeEmptyError("El mazo está vacío.")
        return self.cartas.extraer(0)

    def poner_carta_arriba(self, carta):
        self.cartas.agregar_al_inicio(carta)

    def __len__(self):
        return len(self.cartas)

