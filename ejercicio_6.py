# Bucles [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicio de secuencias numéricas

# Pedir por consola dos números que representen el principio y fin de una
# secuencia numérica.
# Realizar un bucle "for" que recorra esa secuencia armada con "range"
# y cuente cuantos números son negativos y cuantos números son mayor o igual a cero
# Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
# sino que va hasta el anterior

inicio = int(input('Ingrese el primer número de la secuencia\n'))
fin = int(input('Ingrese el último número de la secuencia\n'))

cant_num_pos = 0  # Inicializo el contador en 0
cant_num_neg = 0

# for ... in range(....)

for numeral in range(inicio, fin):
    
    if (numeral % 2) == 0:
        cant_num_pos += 1
    else:
        cant_num_neg += 1

print ("La cantidad de numeros positivos es:", cant_num_pos)
print ("La cantidad de numeros negativos es:", cant_num_neg)


      
    
    
    
    
    



# Imprimir el valor de la cantidad de números positivos y negativos

print("terminamos!")
