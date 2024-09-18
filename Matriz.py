import numpy as np
import time

def crear_matriz(alumnos, materias):
    return np.random.randint(0, 101, size=(alumnos, materias))

def buscar_matriz_1(matriz, alumno, materia):
    return matriz[alumno, materia]

def buscar_matriz_2(matriz, materia, alumno):
    return matriz[materia, alumno]

def medir_tiempo(func, *args):
    inicio = time.time()
    resultado = func(*args)
    fin = time.time()
    return resultado, fin - inicio

alumnos = 500 
materias = 6  

matriz_1 = crear_matriz(alumnos, materias)  
matriz_2 = crear_matriz(materias, alumnos)  

alumno = 321
materia = 5

resultado_1, tiempo_1 = medir_tiempo(buscar_matriz_1, matriz_1, alumno, materia)

resultado_2, tiempo_2 = medir_tiempo(buscar_matriz_2, matriz_2, materia, alumno)

print(f"Resultado en Matriz 1 (alumno 321, materia 5): {resultado_1}, Tiempo: {tiempo_1} segundos")
print(f"Resultado en Matriz 2 (materia 5, alumno 321): {resultado_2}, Tiempo: {tiempo_2} segundos")

def prueba_diferentes_tamanos():
    for alumnos, materias in [(1000, 100), (10000, 500), (100000, 10000)]:
        print(f"\nPrueba con {alumnos} alumnos y {materias} materias")
        
        matriz_1 = crear_matriz(alumnos, materias)
        matriz_2 = crear_matriz(materias, alumnos)
        
        resultado_1, tiempo_1 = medir_tiempo(buscar_matriz_1, matriz_1, 321, 5)
        resultado_2, tiempo_2 = medir_tiempo(buscar_matriz_2, matriz_2, 5, 321)
        
        print(f"  Matriz 1: Tiempo {tiempo_1} segundos")
        print(f"  Matriz 2: Tiempo {tiempo_2} segundos")

prueba_diferentes_tamanos()
