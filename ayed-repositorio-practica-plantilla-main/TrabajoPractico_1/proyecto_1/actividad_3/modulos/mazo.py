# mazo.py


from modulos.ListaDobleEnlazada import ListaDobleEnlazada
from modulos.carta import Carta

class DequeEmptyError(Exception):
    pass  # Define una excepción personalizada para cuando el mazo está vacío

class Mazo:
    def __init__(self):
        self.cartas = ListaDobleEnlazada()

    def esta_vacio(self):
        return len(self.cartas) == 0

    def poner_carta_abajo(self, carta):
        self.cartas.agregar_al_final(carta)


    def sacar_carta_inicio(self):
        if self.esta_vacio():
            raise DequeEmptyError("El mazo está vacío.")
        return self.cartas.extraer(0)

    # def extraer_carta_final(self):
    #     if self.esta_vacio():
    #         raise DequeEmptyError("El mazo está vacío.")
    #     return self.cartas.extraer() 

    def mezclar(self):
        import random
        elementos = [self.extraer_carta_inicio() for _ in range(len(self.cartas))]
        random.shuffle(elementos)
        for carta in elementos:
            self.agregar_carta_final(carta)

    def cantidad_cartas(self):
        return len(self.cartas)

if __name__ == "__main__":
    mazo = Mazo()
    mazo.agregar_carta(Carta("As", "Corazones"))
    mazo.agregar_carta(Carta("Rey", "Diamantes"))
    mazo.agregar_carta(Carta("Reina", "Tréboles"))

    print(f"Cantidad de cartas en el mazo: {mazo.cantidad_cartas()}")
    print(f"Sacando carta del inicio: {mazo.sacar_carta_inicio()}")
    print(f"Cantidad de cartas en el mazo después de sacar una: {mazo.cantidad_cartas()}")
    print({mazo.sacar_carta_inicio()})
    print({mazo.cantidad_cartas()})

