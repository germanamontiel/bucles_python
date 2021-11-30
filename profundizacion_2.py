# Bucles [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Realice una calculadora:
Dentro de un bucle se debe ingresar por línea de comando dos números
Luego se ingresará como tercera entrada al programa el símbolo de la operación
que se desea ejecutar:
- Suma (+)
- Resta (-)
- Multiplicación (*)
- División (/)
- Exponente/Potencia (**)
Se debe efectuar el cálculo correcto según la operación ingresada por consola
Imprimir en pantalla la operación realizada y el resultado

El programa se debe repetir dentro del bucle hasta que como operador
se ingrese la palabra "FIN", en ese momento debe terminar el programa

Se debe debe imprimir un cartel de error si el operador ingresado no es
alguno de lo soportados o no es la palabra "FIN".
'''

print("Mi Calculadora (^_^)")
# Empezar aquí la resolución del ejercicio

numero_1 = int(input("Ingrese un numero: "))
numero_2 = int(input("Ingrese otro numero: "))

metodo = str(input("Ingrese modo a calcular (+,-,*,/,**,: "))

suma = 0
resta = 0
multi = 0
divi = 0
pote = 0

while metodo != "fin":

    if metodo == "+":
        suma = numero_1 + numero_2
        print ("El resultado de la suma es:", suma)
        metodo = str(input("Ingrese modo para continuar - fin para salir: "))

    elif metodo == "-":
        resta = numero_1 - numero_2
        print ("El resultado de la resta es: ", resta)
        metodo = str(input("Ingrese modo para continuar - fin para salir: "))

    elif metodo == "*":
        multi = numero_1 * numero_2
        print ("El resultado de la multiplicacion es: ", multi)
        metodo = str(input("Ingrese modo para continuar - fin para salir: "))

    elif metodo == "/":
        divi = numero_1 / numero_2
        print ("El resultado de la division es: ", divi)
        metodo = str(input("Ingrese modo para continuar - fin para salir: "))

    elif metodo == "**":
        pote = numero_1 ** numero_2
        print("El resultado de la potencia es: ", pote)
        metodo = str(input("Ingrese modo para continuar - fin para salir: "))

    elif metodo == "" or " ":
        print("ingrese una opcion correcta: ")
        metodo = str(input("Ingrese modo para continuar - fin para salir: "))

    else:
        print("ingrese una opcion correcta: ")
        metodo = str(input("Ingrese modo para continuar - fin para salir: "))

print("Gracias por calcular con nosotros")


