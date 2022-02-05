from operator import le
from typing import TextIO


def run():
    # for contador in range (1001):
    #     if contador % 2 != 0: #todo numero que sea impar no se va a imprimir
    #         continue #al decir continue nos estamos brincando a imprimir el siguiente que si cumpla la condicion
    #     print(contador)

    # for i in range(10000):
    #     print(str(i))
    #     if i == 5678:
    #         break    
    #en este caso le esto diciendo al ciclo que cuando i
    # sea igual a 5678 se detenga


    #recorrer un strin
    texto = input('Escribe un texto: ')
    for letra in texto:
        if letra == 'o':
            break
        print(letra)
if __name__ == '__main__':
    run()
