
from modules.grafo import leer_grafo, prim, construir_arbol_desde_predecesor, suma_distancias_arbol


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

    dist, pred = prim(graf, origen)
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


if __name__ == "__main__":
    main()