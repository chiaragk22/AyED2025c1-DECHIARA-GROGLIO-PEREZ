import unittest
import random
import time
from modules.Ordenamientos import ordenamiento_burbuja, ordenamiento_quicksort
from modules.Ordenamientos import ordenamiento_redix as ordenar_por_residuos

# filepath: proyecto_1/modules/test_Ordenamientos.py


class TestOrdenamientos(unittest.TestCase):

    def test_ordenamiento_burbuja(self):
        for size in range(1, 1001):
            lista = [random.randint(1, 10000) for _ in range(size)]
            lista_esperada = sorted(lista)
            start_time = time.time()
            ordenamiento_burbuja(lista)
            end_time = time.time()
            self.assertEqual(lista, lista_esperada)
            print(f"Bubble Sort - Size: {size}, Time: {end_time - start_time:.6f} seconds")

    def test_ordenamiento_quicksort(self):
        for size in range(1, 1001):
            lista = [random.randint(1, 10000) for _ in range(size)]
            lista_esperada = sorted(lista)
            start_time = time.time()
            lista_ordenada = ordenamiento_quicksort(lista)
            end_time = time.time()
            self.assertEqual(lista_ordenada, lista_esperada)
            print(f"Quick Sort - Size: {size}, Time: {end_time - start_time:.6f} seconds")

    def test_ordenar_por_residuos(self):
        for size in range(1, 1001):
            lista = [random.randint(1, 10000) for _ in range(size)]
            lista_esperada = sorted(lista)
            start_time = time.time()
            ordenar_por_residuos(lista)
            end_time = time.time()
            self.assertEqual(lista, lista_esperada)
            print(f"Radix Sort - Size: {size}, Time: {end_time - start_time:.6f} seconds")

if __name__ == "__main__":
    unittest.main()
