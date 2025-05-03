# "Diseño y Evaluación de Algoritmos y TADs".


En el trabajo práctico implementamos y analizamos tres algoritmos de ordenamiento (burbuja, Quicksort y radix sort), desarrollamos una estructura de
datos personalizada (Lista doblemente enlazada) y simulamos el juego de cartas “Guerra” utilizando la estructura creada anteriormente. 

El objetivo del trabajo es comparar los tiempos de ejecución y complejidad entre los diferentes algoritmos, así como utilizar estructuras dinámicas en contextos prácticos, en este caso un juego de cartas.


# Estructura general del código:

El proyecto está dividido en tres carpetas principales: actividad_1, actividad_2, y actividad_3.

- actividad_1/: contiene implementaciones de los algoritmos de ordenamiento, scripts de medición de tiempos y generación de gráficas.
- actividad_2/: implementa la clase ListaDobleEnlazada con los métodos especificados en el enunciado y scripts de prueba y análisis de rendimiento.
- actividad_3/: contiene la implementación del  juego “Guerra” basado en una clase Mazo, que utiliza la ListaDobleEnlazada. Incluye las pruebas
unitarias necesarias.

Las gráficas de los resultados están disponibles en la carpeta data/.

El informe de los resultados de cada problema están disponibles en la carpeta docs/.


# Dependencias:

- Python 3.x
- matplotlib
- random
- time
- pytest (opcional para pruebas unitarias)
- Todas las dependencias están listadas en “deps/requirements.txt”.


# Como ejecutar el proyecto:

1. Clonar o descargar este repositorio.
2. Crear y activar un entorno virtual:
   	“python -m venv venv”
   	“source venv/bin/activate  # o .
	\venv\Scripts\activate en Windows”
3. Instalar las dependencias:
   	“pip install -r deps/requirements.txt”
4. Ejecutar los scripts correspondientes en
cada carpeta (problema1, problema2,
problema3).


# AUTORES:
 
- Carolina Belén Pérez
- Chiara Groglio Kremer
- Ignacio Dechiara
