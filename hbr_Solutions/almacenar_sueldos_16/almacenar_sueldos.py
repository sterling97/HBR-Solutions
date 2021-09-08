# 16) Se debe crear un vector donde almacenar 5 sueldos. 
# Ordenar el vector sueldos de menor a mayor.

salaries = [2500, 8000, 7010, 6200, 3200]
lowest_salaries = salaries[0]


for x in range(0, 5):
    if (salaries[x] < lowest_salaries):
        lowest_salaries = salaries[x]


salaries.sort()


print(f"{salaries}" + "\n")
print("El salario mas bajo es: $" + str(lowest_salaries) + "\n")

