import random

option =["piedra", "tijera", "papel"]

print("Hola, jugemos cachipun")

print("ingresa su opcion")
print(1,"piedra")
print(2,"tijera")
print(3,"papel")

user_input = int(input("jugador1\n"))
user_option = option[user_input - 1]

computer_option = random.choice(options)

print("mi mano: ", user_option)
print("mano del computador:", computer_option)

if (user_option == computer_option):
    print("empatan jugadores")
elif (user_option == "piedra" and computer_option == "tijera") or (user_option == "tijera" and computer_option == "papel") or (user_option == "papel" and computer_option == "piedra"):
    print(" felicidades! ganaste esta partida")
else:
    print("lo siento, el computador ha ganado")






















0