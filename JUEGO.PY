# Juego Piedra, Papel o Tijera

print("=== PIEDRA, PAPEL O TIJERA ===")

# Entrada de datos
jugador1 = input("Jugador 1, elige piedra, papel o tijera: ").lower()
jugador2 = input("Jugador 2, elige piedra, papel o tijera: ").lower()

# Verificar si las elecciones son iguales
if jugador1 == jugador2:
    print("Empate. Ambos eligieron la misma jugada.")

# Verificar si gana el Jugador 1
elif (jugador1 == "piedra" and jugador2 == "tijera") or \
     (jugador1 == "papel" and jugador2 == "piedra") or \
     (jugador1 == "tijera" and jugador2 == "papel"):
    print("Gana el Jugador 1.")

# Si no ganó el Jugador 1, gana el Jugador 2
else:
    print("Gana el Jugador 2.")
# Mostrar resultado
print("Fin del juego.")