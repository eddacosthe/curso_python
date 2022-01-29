#def imprimir_mensaje():
#    print("mensaje especial: ")
#    print("¡Estoy aprendiendo a usar funciones!")


#imprimir_mensaje()


opcion = int(input("elige una opcion (1, 2 ,3):"))

def elegir_opcion(mensaje):
    print('Hola')
    print('Como estas?')
    print(mensaje)
    print('Adios Baby')



if opcion == 1:
   elegir_opcion('Elegiste la opcion 1')
    
elif opcion == 2:
    elegir_opcion('Elegiste la opcion 2')

elif opcion == 3:
    elegir_opcion('Elegiste la opcion 3')
else:
    print('tu opcion no es correcta')