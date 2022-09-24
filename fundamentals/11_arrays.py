# Los arreglos (listas) son estructuras de datos fundamental
# Que permite agrupar  valores, separados por coma

first_array = ["sacar la basura", "peinarse", "dormir", "secar la ropa"]

# En python el primer elemento de un arreglo tiene posicion (indice) 0
print(first_array[0])
print(first_array[1])
print(first_array[2])
print(first_array[3])

# No existe el elemento con indice 4 y python  da error
# print(first_array[4])

# Podemos saber el largo de un arreglo o lista de la funcion pre definida len()
print(len(first_array))

# Ademas, podemos agregar elementos al arreglo
first_array.append("comer")
first_array.append("dormir")

# Podemos indicar la posoción del nuevo elemento a agregar con insert
first_array.insert(0,"levantarse")
# Podemos imprimir la lista completa
print(first_array)




