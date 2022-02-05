def run():
    peso = int(input('Ingresa tu peso: '))
    altura =int(input('Ingresa tu altura en cm: '))
    altura = altura /100
    imc = (peso / altura**2)
    print('tu indice de masa corporal es: '+str(round(imc,2)))




if __name__ =='__main__':
    run()