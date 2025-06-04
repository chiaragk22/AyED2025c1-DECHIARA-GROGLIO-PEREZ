# Trabajo Práctico N°2: Base de Datos de Temperaturas con AVL

## 1. Estructura de archivos

- **avl.py**  
  Implementación genérica de un árbol AVL.
- **temperaturas_db.py**  
  Clase `Temperaturas_DB` que envuelve `AVLTree` para almacenar temperaturas por fecha.
- **prueba_temperaturas.py**  
  Script de prueba que inserta datos, realiza consultas y muestra resultados.
- **README.md**  
  Este archivo.

## 2. Análisis de complejidad

- `AVLTree.insertar(clave, valor)`: O(log n)  
- `AVLTree.buscar(clave)`: O(log n)  
- `AVLTree.eliminar(clave)`: O(log n)  
- `AVLTree.recorrido_en_rango(c1, c2)`: O(k + log n)  

- `Temperaturas_DB.guardar_temperatura(...)`: O(log n)  
- `Temperaturas_DB.devolver_temperatura(...)`: O(log n)  
- `Temperaturas_DB.borrar_temperatura(...)`: O(log n)  
- `Temperaturas_DB.cantidad_muestras()`: O(n)  
- `Temperaturas_DB.devolver_temperaturas(c1, c2)`: O(k + log n)  
- `Temperaturas_DB.max_temp_rango(c1, c2)`: O(k + log n)  
- `Temperaturas_DB.min_temp_rango(c1, c2)`: O(k + log n)  
- `Temperaturas_DB.temp_extremos_rango(c1, c2)`: O(k + log n)  

> Donde *n* es el número total de nodos (fechas) en el árbol, y *k* es la cantidad de nodos en el rango especificado.

## 3. Instrucciones de uso

1. Clonar el repositorio:  
   ```bash
   git clone https://github.com/chiaragk22/AyED2025c1-DECHIARA-GROGLIO-PEREZ.git
   cd AyED2025c1-DECHIARA-GROGLIO-PEREZ/TP2_TemperaturasDB


## Autores:
 
- Carolina Belén Pérez
- Chiara Groglio Kremer
- Ignacio Dechiara