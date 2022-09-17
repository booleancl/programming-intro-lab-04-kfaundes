# la función principal para manejar archivos es open()
# Ests función recive dos parámetros, el nombre del archivo y el modo
# Los modos son:

# r: para leer y da error si el archivo no existe
# a: para realizar append ( agregar al final). si el archivo no existe, lo crea
# w: para escribir. Elimina el contenido anterior si existe.

file = open("file_handling/examples.txt", "r")
print(file.read())