from cola_prioridad import ColaPrioridad

def leer_grafo(path_archivo):
    """
    Lee aldeas.txt y construye un grafo (dict) y un conjunto de aldeas.
    Formatos admitidos:
      - "A, B, 5" (ruta bidireccional con peso 5)
      - "SoloAldea" (nodo sin aristas)
    """
    grafo = {}
    aldeas = set()

    with open(path_archivo, 'r', encoding='utf-8') as f:
        for linea in f:
            linea = linea.strip()
            if not linea or linea.startswith('#'):
                continue

            partes = [p.strip() for p in linea.split(',')]
            if len(partes) == 3:
                si, ti, di_str = partes
                try:
                    di = int(di_str)
                except ValueError:
                    continue
                aldeas.add(si)
                aldeas.add(ti)
                grafo.setdefault(si, []).append((ti, di))
                grafo.setdefault(ti, []).append((si, di))
            elif len(partes) == 1:
                nodo = partes[0]
                aldeas.add(nodo)
                grafo.setdefault(nodo, [])
            else:
                continue

    # Asegurar que cada aldea aparece en el grafo
    for a in aldeas:
        grafo.setdefault(a, [])

    return grafo, aldeas


def prim_con_monticulo(grafo, origen):
    visitados = set()
    cola = ColaPrioridad()
    predecesor = {nodo: None for nodo in grafo}
    dist = {nodo: float('inf') for nodo in grafo}
    dist[origen] = 0

    cola.encolar(0, origen)

    while not cola.esta_vacia():
        costo, nodo = cola.desencolar()
        if nodo is None or nodo in visitados:
            continue
        visitados.add(nodo)

        for vecino, peso in grafo[nodo]:
            if vecino not in visitados and peso < dist[vecino]:
                dist[vecino] = peso
                predecesor[vecino] = nodo
                cola.encolar(peso, vecino)

    return dist, predecesor



def construir_arbol_desde_predecesor(predecesor):
    """
    Convierte diccionario predecesor en:
      - hijos[node]: lista de nodos que dependen de 'node'
      - aristas_arbol: lista de pares (padre, hijo)
    """
    hijos = { nodo: [] for nodo in predecesor }
    aristas_arbol = []

    for nodo, padre in predecesor.items():
        if padre is not None:
            hijos[padre].append(nodo)
            aristas_arbol.append((padre, nodo))

    return hijos, aristas_arbol

def suma_distancias_arbol(grafo, aristas_arbol):
    """
    Suma los pesos de las aristas que forman parte del árbol de rutas mínimas.
    """
    total = 0
    for (padre, hijo) in aristas_arbol:
        for (v, peso) in grafo[padre]:
            if v == hijo:
                total += peso
                break
    return total


