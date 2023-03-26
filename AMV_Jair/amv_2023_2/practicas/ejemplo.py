import numpy as np # Importamos numpy como np


def generarNumeros(n: int = 10000, media: float = 0, desv: float = 1) -> np.array: # Definimos la función
    """Genera un Array de Numpy de números pseudo aleatorios 
    con distribución normal. 

    Args:
        n (int): Tamaño del array
        media (float): Media de la distribución
        desv (float): Desviación estándar de la distribución

    Returns:
        np.array: Array con los números normales
    """
    x = np.random.normal(loc=media, scale=desv, size=n) # Generamos los números
    return x # Regresamos el array


def escribirArchivo(nombre: str, numeros: np.array): # Definimos la función
    """Escribe un array en un archivo de texto, si los números son negativos
    entonces escribe un cero.

    Args:
        nombre (str): nombre (ruta) del archivo a escribir
        numeros (np.array): array con los números normales
    """
    with open(nombre, 'w') as f: # Abrimos el archivo en modo escritura
        for num in numeros:      # Iteramos sobre el array
            if num < 0:          # Si el número es negativo
                num = 0          # Lo ponemos en cero
            f.write(str(num)+'\n') # Escribimos el número y un salto de línea
        f.close() # Cerramos el archivo


if __name__ == '__main__':  # Si el archivo es el principal
    # Funcionalidad principal
    escribirArchivo('normal.txt', generarNumeros(100, 100, 24)) # Escribimos el archivo
