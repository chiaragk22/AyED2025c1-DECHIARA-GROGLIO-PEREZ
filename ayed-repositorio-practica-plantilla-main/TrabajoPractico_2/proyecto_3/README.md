# Trabajo Práctico N°2: 
# Actividad 3: Palomas mensajeras

## 1. Estructura del proyecto

- **aldeas_txt**  
  El archivo aldeas.txt contiene la descripción del mapa de aldeas, con las conexiones entre ellas y sus distancias
  expresadas en leguas. Se usa como entrada para construir el grafo del problema.

En la carpeta modules:
- **grafo.py**: implementación del algoritmo Prim y demás funciones
- **main.py**: ejecución general del código usando las funciones del archivo grafo.py
- **Monticulo.py**: 
  Implementación genérica de un Montículo Binario.
- **ColaPrioridad.py**  
  La clase `ColaPrioridad` contiene una cola con prioridades mínimas basada en el montículo binario, donde cada elemento se encola según una función de prioridad personalizada.

En la carpeta docs:
- **doc_act3.pdf**: contiene un informe detallado de este proyecto