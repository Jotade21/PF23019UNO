# PF23019UNO-Libreria de Métodos Numéricos

Esta librería implementa métodos numéricos para resolver sistemas de ecuaciones lineales y no lineales.

## Instalación
```bash
pip install PF23019UNO

## Métodos Implementados

### Sistemas Lineales
- Eliminación de Gauss
- Gauss-Jordan
- Regla de Crammer
- Descomposición LU
- Método de Jacobi
- Método de Gauss-Seidel

### Sistemas No Lineales
- Método de Bisección



## Ejemplo de Uso
# Resolver un sistema de ecuaciones lineales
import numpy as np
from PF23019UNO import eliminacion_gauss  # o el método que desees usar

if __name__ == "__main__":
    print("Problema de ejemplo:")
    A = [
        [3, 1, -1],
        [2, 4, 1],
        [-1, 2, 5]
    ]
    b = [4, 1, 1]

    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)

    print(f"Matriz A:\n{A}\n")
    print(f"Vector b:\n{b}\n")

    solucion = eliminacion_gauss(A, b)
    print(f"\nSolución final (Gauss): {solucion}\n")

##Encontrar la raíz de una función no lineal con bisección
from PF23019UNO import biseccion

if __name__ == "__main__":
    f = lambda x: x**2 - 4  # Raíz en x = 2 y x = -2
    a = 0
    b = 5

    try:
        raiz = biseccion(f, a, b)
        print(f"La raíz aproximada es: {raiz:.8f}")
    except ValueError as e:
        print(f"Error: {e}")

### Documentación de Funciones
eliminacion_gauss(A, b)
Resuelve un sistema 𝐴𝑥=𝑏
Ax=b usando eliminación hacia adelante y sustitución hacia atrás.

gauss_jordan(A, b)
Convierte la matriz aumentada en forma reducida para obtener directamente la solución.

crammer(A, b)
Aplica la regla de Cramer utilizando determinantes para resolver el sistema.

descomposicion_LU(A, b)
Utiliza descomposición LU (requiere implementación con SciPy o personalizada).

jacobi(A, b, x0=None, tol=1e-10, max_iter=1000)
Método iterativo para encontrar una solución aproximada.

gauss_seidel(A, b, x0=None, tol=1e-10, max_iter=1000)
Versión optimizada del método de Jacobi que usa los valores actualizados en cada paso.

biseccion(f, a, b, tol=1e-10, max_iter=1000)
Encuentra una raíz de la función f en el intervalo [a,b] usando el método de bisección.

## Autor
Josue David Parada Flores-PF23019 - Métodos Numéricos

