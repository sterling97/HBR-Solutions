

burgers_price = 2 
chips_price = 1.2
drinks_price = 0.8

client_burgers = int(input('Cuantas hamburguesas desea?: '))
client_chips = int(input('Cuantas papas fritas desea?: '))
client_drinks = int(input('Cuantas bebidas desea?: '))

to_pay = (burgers_price * client_burgers) + (chips_price * client_chips) + (drinks_price * client_drinks)

print(f"Valor a pagar {to_pay}")