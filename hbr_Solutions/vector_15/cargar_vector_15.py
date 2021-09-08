# 15) Cargar un vector de n elementos. imprimir el menor y un mensaje si se repite 
# dentro del vector.


vectors = [32, 5, 87, 55, 12, 4, 23, 1, 65, 17, 5]
menor = vectors[0]


for x in range(0, 10):
    if (vectors[x] < menor):
        menor = vectors[x]


print(f"{vectors}" + "\n")
print("El menor vector es: " + str(menor) + "\n")


numeros = vectors


repetidos = []
archivo = []


for n in numeros:
    if n not in archivo:
        archivo.append(n)
    else:
        repetidos.append(n)


print(f"El numero que se repite es: {repetidos}")





















