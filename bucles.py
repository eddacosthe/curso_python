
from ast import While

def potencia(contador):
    pass


def run(): #definicmos la funcion principal eso siempre es de ley
    LIMITE = 1000000 #esto es una  constante y como cual el nombre se escribe en mayusculas
    contador = 0
    potencia_2 = 2**contador
    while potencia_2 < LIMITE:
        print('2 elevado a  '+ str(contador) + ' es igual a: ' + str(potencia_2))
        contador = contador + 1
        potencia_2 = 2**contador


 


if __name__ == '__main__':
    run()