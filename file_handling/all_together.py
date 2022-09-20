
print("Bienvenido al programa")
user_input= ""

while user_input != "exit":
  print("ingresa una opción")
  print("1", "agregar contenido")
  print("2", "leer contendido")
  print("exit", "para salir")

  user_input = input()

    if user_input == "1":
       file = open("demo_two.txt", "a")   
       user_content = input("ingresa el contenido")
       file.write(user_content)
       file.close()
    elif user_input == "2":
       file = open("demo_two", "r") 
    for line in file:
        print(line)
    else:
        print("opción incorrecta")

 print("chau chau")            