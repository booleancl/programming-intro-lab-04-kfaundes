# hasta ahora todos los selementos primitivos que hemos manejados
#listas, diciionarios, string, number, etc tienen un cierti tiempo
# que vemos con el método especial type()

print(type(1))
print(type(["a","b", "c",]))
print(type(True))
print(type("hello world"))

class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def say_name(self):
        print("mi nombre es", self.name,"y tengo",self.age,"años")
        
firulais = Dog("firulais", 4)
lulu = Dog("lulu", 3)
print(type(firulais))

firulais.say_name()
lulu.say_name()

