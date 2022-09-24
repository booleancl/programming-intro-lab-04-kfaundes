# Las funciones pueden hacer cosas y tambien pueden retonar valores

def circle_area(radius):
    area =3.1415*radius**2
    return area

# En este caso la funcion me entrega o devuelve  el valor

result = circle_area(4)
print(result)

def circle_volume(radius,heigth):
    volume = 3.1415*radius**2*heigth
    return volume
result_two =circle_volume(4,10)
print(result_two)
print(area)


