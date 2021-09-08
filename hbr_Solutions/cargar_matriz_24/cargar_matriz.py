# 24) Crear una matriz de n * m filas (cargar n y m por teclado) Imprimir los cuatro valores que se
# encuentran en los vértices de la misma (mat[0][0] etc.)



matrix = []

rows = int(input("Cantidad de Filas: "))
columns = int(input("Cantidad de columnas: "))


for i in range(rows):
    matrix.append([0]  * columns)
    matrix.append([1]  * columns)

for rows in range(rows):
    for columns in range(columns):
        matrix[rows] [columns] = int(input("Elemento %d, %d : " % (rows,columns)))

print(matrix)
print(f'los cuatro primeros vectores son {matrix[0]}y {matrix[1]}')
