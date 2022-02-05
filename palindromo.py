def palindromo(palabra):
    #primero le vamos a quitar los espacios a a la palabra
    palabra = palabra.replace(' ','')
    #pasar la palabra a minusculas o mayusculas
    palabra = palabra.lower()
    #despues vamos a leer la plabra de manera invertida y a guardarla
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False



def run():
    palabra = input("Escribe una palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("Es palindromo")
    else:
        print("No es palindromo")


if __name__ == '__main__':
    run()

