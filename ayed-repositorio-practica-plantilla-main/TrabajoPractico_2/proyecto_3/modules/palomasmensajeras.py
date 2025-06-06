import heapq

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

def dijkstra_con_predecesor(grafo, origen):
    """
    Dijkstra que devuelve distancias mínimas y predecesor para cada nodo.
    """
    dist = { nodo: float('inf') for nodo in grafo }
    predecesor = { nodo: None for nodo in grafo }
    dist[origen] = 0
    heap = [(0, origen)]

    while heap:
        d_actual, nodo = heapq.heappop(heap)
        if d_actual > dist[nodo]:
            continue

        for (vecino, peso) in grafo[nodo]:
            nueva_d = d_actual + peso
            if nueva_d < dist[vecino]:
                dist[vecino] = nueva_d
                predecesor[vecino] = nodo
                heapq.heappush(heap, (nueva_d, vecino))

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

def main():
    # 1) Leer el grafo desde "aldeas.txt"
    graf, aldeas = leer_grafo("aldeas.txt")

    # 2) Mostrar lista de aldeas en orden alfabético
    orden = sorted(aldeas)
    print("1) Lista de aldeas en orden alfabético:")
    for a in orden:
        print(f"   - {a}")
    print()

    # 3) Ejecutar Dijkstra desde "Peligros"
    origen = "Peligros"
    if origen not in graf:
        raise ValueError(f"'{origen}' no está en el grafo")

    dist, pred = dijkstra_con_predecesor(graf, origen)
    hijos, arbol = construir_arbol_desde_predecesor(pred)

    # 4) Mostrar la información de transmisión por aldea
    print("2) Rutas de transmisión de noticias:")
    for aldea in orden:
        if aldea == origen:
            recibida_de = "(origen)"
        else:
            recibida_de = pred[aldea] if pred[aldea] is not None else "(no llega)"

        envia_a = sorted(hijos[aldea]) if hijos[aldea] else "ninguna"

        print(f"   - {aldea}: recibe de → {recibida_de}; envía a → {envia_a}")
    print()

    # 5) Calcular y mostrar la distancia total recorrida
    total_dist = suma_distancias_arbol(graf, arbol)
    print(f"3) Distancia total recorrida por todas las palomas: {total_dist} leguas")

# def main():
#     # 1) Leer el grafo desde "aldeas.txt"
#     graf, aldeas = leer_grafo("aldeas.txt")

#     # 2) Mostrar lista de aldeas en orden alfabético
#     orden = sorted(aldeas)
#     print("1) Lista de aldeas en orden alfabético:")
#     for a in orden:
#         print("   -", a)
#     print()

#     # 3) Dijkstra desde "Peligros"
#     origen = "Peligros"
#     if origen not in graf:
#         raise ValueError(f"'{origen}' no está en el grafo")

#     dist, pred = dijkstra_con_predecesor(graf, origen)
#     hijos, arbol = construir_arbol_desde_predecesor(pred)

#     # 4) Mostrar árbol de envío más eficiente
#     print("2) Árbol de envío más eficiente (recibe de → envía a):")
#     for a in orden:
#         if a == origen:
#             recibido = "(origen)"
#         else:
#             recibido = pred[a] if pred[a] is not None else "(no llega)"
#         emisor = hijos[a]
#         print(f"   - {a}: recibe de → {recibido};  envía a → {emisor}")
#     print()

#     # 5) Sumar distancias totales recorridas
#     total_dist = suma_distancias_arbol(graf, arbol)
#     print(f"3) Distancia total recorrida por todas las palomas: {total_dist} leguas")

if __name__ == "__main__":
    main()
