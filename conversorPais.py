def conversor(tipo_pesos,valor_dolar):
    pesos = input("¿Cuantos pesos "+tipo_pesos +" tienes? ")
    pesos = float(pesos)
    valor_dolar = 104
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes "+ dolares +" dolares")



menu = """
Bienvenido al conversor de monedas 🪙🪙

1 - Pesos Argentinos
2 - Pesos Colombianos
3 - Pesos Mexicanos
Selecciona la opcion: """
opcion = int(input(menu))
if opcion == 1:
    conversor("Argentinos",104)
elif opcion == 2:
    conversor("Colombianos",3958)
    
elif opcion == 3:
   conversor("Mexicanos",20)
else:
    print("opcion invalida")