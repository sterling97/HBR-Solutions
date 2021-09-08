import pandas as pd
import math
import numpy as np


user_number = int(input("Digite un numero: "))

# Valor absoluto es la distancia de un numero al 0.
serie = pd.Series(user_number)
serie.abs()

potencia = user_number**3

raiz_cuadrada = math.sqrt(user_number)

seno = np.sin(user_number)

coseno = np.cos(user_number)

maximo = max(user_number, 50)

minimo = min(user_number, 50)

entero_del_decimal = math.trunc(18.78)

redondear_decimal = round(18.78)

print(f"""Valor absoluto: {serie.abs()}
          Potencia: {potencia}
          Raiz cuadrada: {raiz_cuadrada}
          Seno: {seno}
          Coseno: {coseno}
          Numero maximo: {maximo}
          Numero minimo: {minimo}
          Parte entera del decimal (18.78) es : {entero_del_decimal} 
          Redondeo del decimal (18.78) es: {redondear_decimal}
      """)