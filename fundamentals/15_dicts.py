import math
# Los diccionarios al igual que los arreglos, nos permiten
# guardar colecciones. Pero accedemos a sus elementos mediante la llave.


student = {
  "name": "Bob",
  "lastname": "Esponja",
  "grades": [7,6.5,7,6.6,5],
  "address": "Casa piña en el fondo de bikini",
}

# Sumar todas las notas y dividir por la cantidad de notas
# La variable auxiliar nos sirve de acumulador
aux_sum = 0
for grade in student["grades"]:
  aux_sum = aux_sum + grade

# alternativamente, podemos sumar directamente pasando el arreglo a la función 
# math.fsum, que sirve para sumar floats
alternative_sum = math.fsum(student["grades"])

average = alternative_sum/len(student["grades"])


print("Nombre:", student["name"], student["lastname"])
print("Dirección:", student["address"])
print("Promedio de notas:", average)

# Si queremos sumar números enteros, tenemos una opcion mas simples
# que es la funcíon sum()

numbers = (1,2,3,)

last_sum = sum(numbers)

print(last_sum)