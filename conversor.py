pesos = input("¿cuantos pesos tienes?: ")
pesos = float(pesos)
valor_dolar = 22
dolares = pesos / valor_dolar
dolares = round(dolares,2)
dolares = str(dolares)
print("Tienes $"+  dolares + " dolares")
dolares = input("¿cuantos dolares tienes?: ")
dolares = float(dolares)
dolares = pesos * valor_dolar
dolares = round(dolares,2)
dolares = str(dolares)
print("Tienes $"+  dolares + " pesos")