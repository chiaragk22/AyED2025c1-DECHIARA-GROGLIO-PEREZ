from modulos.juego_guerra import JuegoGuerra
import random

if __name__ == "__main__":
    n = random.randint(0, 1000)
    juego = JuegoGuerra(random_seed=n)
    juego.iniciar_juego()
