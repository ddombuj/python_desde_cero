############################################################
###                       CALCULADORA                    ###
############################################################
# 17/06/2025    Diego Domínguez #
#################################

## Variables globales
opcionElegida = 1


## Funciones
def imprimirMenu():
    opcionValida = False
    opcion = None
    while opcionValida == False :
        try:
            print('\n-------Menu-------')
            print('1. Sumar')
            print('2. Restar')
            print('3. Multiplicar')
            print('4. Dividir')
            print('0. Salir')
            print('------------------')
            opcion = int(input('Introduce el número de la opcion a elegir: '))
        except ValueError:
            print("Opción no valida, inténtalo de nuevo...")
            print("...\n")
        else:
            if opcion < 0 or opcion > 4 :
                print("Opción no valida, inténtalo de nuevo...")
                print("...\n")
            else:
                opcionValida = True
    # end while
    return opcion

def leerNumeros():
    print("(Introduce un caracter para salir)")
    num1 = input("Introduce el primer número: ")
    try:
        num1 = float(num1)
        num2 = input("Introduce el segundo número: ")
        num2 = float(num2)
        return num1,num2
    except:
        print("No es un número... Saliendo\n")



def sumar():
    print("\n----Suma----")
    try:
        num1,num2 = leerNumeros()
        print(num1," + ",num2," = ",num1 + num2)
    except:
        pass
def restar():
    print("\n----Resta----")
    try:
        num1,num2 = leerNumeros()
        print(num1," - ",num2," = ",num1 - num2)
    except:
        pass
def multiplicar():
    print("\n----Multiplicación----")
    try:
        num1,num2 = leerNumeros()
        print(num1," x ",num2," = ",num1 * num2)
    except:
        pass
def dividir():
    print("\n----División----")
    try:
        num1,num2 = leerNumeros()
        try:
            print(num1," / ",num2," = ",num1 / num2)
        except:
            print("No es posible dividir entre 0\n")
    except:
        pass

## Main

# Bucle que no termina hasta que se elija la opción de salir
while opcionElegida != 0 :
    opcionElegida = imprimirMenu()
    match opcionElegida:
        case 0:
            break
        case 1:
            sumar()
        case 2:
            restar()
        case 3:
            multiplicar()
        case 4:
            dividir()
print("Saliendo...")




