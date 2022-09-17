# Podemos leer las lineas de un archivo utilizando la estructuras de control for, Ejemplo
file = open("file_hanadling/examples.txt")

line_number = 1
for line in file:
    print(line_number, line)
    # line_number =line_number + 1
    line_number += 1


file.close()