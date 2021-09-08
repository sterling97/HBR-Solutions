# 23) Crear una matriz de n * m filas (cargar n y m por teclado) Intercambiar la primer fila con la segundo.
# Imprimir luego la matriz.


import numpy as np


m = np.arange(1, 16).reshape(3, -1)
print(m)


m[:, [0, 3, 2, 1, 4]]