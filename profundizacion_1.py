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
Realice un programa que pida por consola dos números que representen
el principio y fin de una secuencia numérica.

Realizar un bucle "for" que recorra esa secuencia armada con "range"
y cuente cuantos números ingresados hay, y la sumatoria de todos los números.

Al finalizar el bucle, utilice la variable "cantidad_numeros" y la variable
"sumatoria" para calcular el promedio de todos los números ingresados.

Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
sino que va hasta el anterior.
'''

print('Comenzamos a ponernos serios!')
# Empezar aquí la resolución del ejercicio

# inicio = ....
ini = int(input("Ingrese un numero:\n"))
fin = int(input("Ingrese otro numero:\n"))
# fin = ....
sumatoria = 0
contador = 0
# cantidad_numeros ....
for i in range(ini,fin):
    contador += 1
print("La cantidad de valores creados son", contador)    
# sumatoria ....
for numeros in range(ini,fin): 
    sumatoria += numeros
print("El resultado de la suma de", numeros, "es igual a: ", sumatoria)

# bucle.....
promedio = 0
# for i in range(ini,fin):
promedio = sumatoria / contador
print("El resultado del promedio entre la cantidad creada\ny la suma de los valores, da como resultado:", promedio)

# Al terminar el bucle calcular el promedio como:
# promedio = sumatoria / cantidad_numeros

# Imprimir resultado en pantalla
