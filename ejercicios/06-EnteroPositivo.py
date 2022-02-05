def run():
    n = int(input('Escribe un numero: '))
    if n < 0:
        print('El numero no es positivo')
    else:
        for i in range(1, n + 1):
            i = int(i)
            suma = (i * (i + 1) ) / 2
            print('la suma de '+ str(i) + ' es '+ str(round(suma)))




if __name__ == '__main__':
    run()

