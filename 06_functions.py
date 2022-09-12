# Una funcion es un grupo de sentencias con un nombre que realizan una computacion.
# Primero uno define una funcion y luego de "llama" o "ejecuta" esa funcion.

# Python viene con muchas funciones listas para usar.
# Solo hay que llamarla o ejecutarlas
print("Hola karen")

# La mayoria de las funciones entregan un valor, es decir, nos devuelve el resultado. Ejemplos

str_num = "32"
real_num = int(str_num ) #Esta funcion transforma a entero
print(type(real_num))

float_num =3.9999
int_num =int(float_num)
print(int_num)

# La siguente linea es un error 
# int ("hola inmundo")

print(float("32")) # Esta funcion entrega un float
print(str(3.1415)) # Esta funcion entrega un str

# Composición de funciones: Anidar funciones

print(str(3.1415))
