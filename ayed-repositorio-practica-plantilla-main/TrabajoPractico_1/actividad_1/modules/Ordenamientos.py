import random
import time

import matplotlib.pyplot as plt


lista_random = [random.randint(10000, 99999) for _ in range(500)]

def ordenamiento_burbuja(lista):
    for num in range(len(lista)-1, 0, -1):
        for x in range(num):
            if lista[x] > lista[x+1]:
                lista[x], lista[x+1] = lista[x+1], lista[x]

lista_ordenada_burbuja = lista_random.copy()
ordenamiento_burbuja(lista_ordenada_burbuja)

def ordenamiento_quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[0]
    menores = [x for x in lista[1:] if x < pivote]
    mayores = [x for x in lista[1:] if x >= pivote]
    return ordenamiento_quicksort(menores) + [pivote] + ordenamiento_quicksort(mayores)

lista_ordenada_quicksort = ordenamiento_quicksort(lista_random.copy())

def ordenamiento_redix(lista):
    def ordenamiento_por_digito(lista, exponente):
        tam = len(lista)
        salida = [0] * tam
        conteo = [0] * 10  

        for numero in lista:
            indice = (numero // exponente) % 10
            conteo[indice] += 1

        for i in range(1, 10):
            conteo[i] += conteo[i - 1]

        i = tam - 1
        while i >= 0:
            indice = (lista[i] // exponente) % 10
            salida[conteo[indice] - 1] = lista[i]
            conteo[indice] -= 1
            i -= 1

        for i in range(tam):
            lista[i] = salida[i]

    maximo = max(lista)
    exponente = 1
    while maximo // exponente > 0:
        ordenamiento_por_digito(lista, exponente)
        exponente *= 10

def medir_tiempos():
    tam = range(1, 1001)
    tiempos_burbuja = []
    tiempos_quicksort = []
    tiempos_redix = []

    for x in tam:
        lista = [random.randint(1, 10000) for _ in range(x)]

        lista_burbuja = lista.copy()
        inicio = time.time()
        ordenamiento_burbuja(lista_burbuja)
        fin = time.time()
        tiempos_burbuja.append(fin - inicio)

        lista_quick= lista.copy()
        inicio = time.time()
        ordenamiento_quicksort(lista_quick)
        fin= time.time()
        tiempos_quicksort.append(fin - inicio)

        lista_redix= lista.copy()
        inicio = time.time()
        ordenamiento_redix(lista_redix)
        fin= time.time()
        tiempos_redix.append(fin - inicio)
    return tam, tiempos_burbuja, tiempos_quicksort, tiempos_redix

