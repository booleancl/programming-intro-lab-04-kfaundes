# hay tres modos para leer un archivo con la función open()

# r: para leer y da error si el archivo no existe
# a: para realizar append ( agregar al final). si el archivo no existe, lo crea
# w: para escribir. Elimina el contenido anterior si existe.

file = open("file_handling/samples.txt", "r", encoding="UTF-8")
# La función open entre un "objeto". Entendemos un objeto
# como algo que tiene "datos" y " metodos". Los metodos con son para
# manipular sus datos

print(file)


# para leer el contenido del objeto file, tenemos el método del objetivo
# read

print(file.read())

# Podemos leer el archivo utilizado for
file = open("file_handling/samples.txt", "r", encoding="UTF-8")

for line in file:
    print(line)

