# Tenemos expresiones que se pueden evaluar en términos booleanos
# Ó dicótomicos
# Ejemplo

print(10 > 9)

# Esto nos permite hacer ejecuciones condicionales, por ejemplo

def is_adult(age): 
  if age >= 18:
    return True
  else:
    return False

gaby_age = 4 
Karen_age = 36

# Estas siguentes instrucciones las podriamos leer como:
# "Si (if) el resultado de is_adult ejecutada con la variable gaby_age o karen_age

# es verdadero, entonces el programa imprime "quieres una cerveza?"
# De otro modo (else), imprime "Cantemos chuchuwa?

if is_adult(karen_age):
  print("Quieres una cerveza?")
else:
  print("Cantemos chuchuwa?")
# elif es una abreviación "else if" nos permite expresiones. podemos tener tantos como se necesita

if karen_age > gaby_age:
  print("karen es mayor que gaby")
elif karen_age < gaby_age:
  print("karen es menor que gaby")
else:
  print("tienen la misma edad gaby y karen")



