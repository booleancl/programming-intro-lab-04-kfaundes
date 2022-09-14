# Similar a los arreglos , los dicionarios nos permiten
# estructurar informacion. Con la diferencia de que los 
# elementos estan ordenados por llave y no por índices, ejemplos

my_car = {
  "brand":"Mazda",
  "model": "5",
  "year": 2022,
  "options":["5 puertas", "Aire acondicionado","Frenos ABS"],
  "available": True
}

print(my_car["brand"])
print(my_car["year"])
print(my_car["options"])

# Si queremos todas las llaves tenemos el método .keys()
print(my_car.keys())
# Si queremos todos los valores, tenemos el método .values()
print(my_car.values())

# Podemos tambíen actualizar valores de una determinada llave

my_car["model"] = "9"
print(my_car["model"])
# Tambien podemos agregar llaves y valores
my_car["color"] = "silver"
print(my_car)
