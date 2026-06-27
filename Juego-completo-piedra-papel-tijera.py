# ==========================================
# PROYECTO: PIEDRA, PAPEL O TIJERA
# Autor: Estudiante
# ==========================================

import random

# -----------------------------
# LISTA DE OPCIONES
# -----------------------------
opciones = ["piedra", "papel", "tijera"]

# -----------------------------
# TUPLA DE MENSAJES
# -----------------------------
mensajes = (
    "¡Excelente jugada!",
    "¡Buen intento!",
    "Sigue practicando."
)

# -----------------------------
# DICCIONARIO DE REGLAS
# -----------------------------
reglas = {
    "piedra": "tijera",
    "tijera": "papel",
    "papel": "piedra"
}

# -----------------------------------
# FUNCIÓN PARA DETERMINAR GANADOR
# -----------------------------------
def determinar_ganador(jugador1, jugador2):

    # Operador relacional ==
    if jugador1 == jugador2:
        return 0

    elif reglas[jugador1] == jugador2:
        return 1

    else:
        return 2


# -----------------------------------
# MODO DOS JUGADORES
# -----------------------------------
def jugar_dos_jugadores():

    print("\n=== MODO DOS JUGADORES ===")

    nombre1 = input("Nombre Jugador 1: ")
    nombre2 = input("Nombre Jugador 2: ")

    puntos1 = 0
    puntos2 = 0

    continuar = "s"

    # Bucle while
    while continuar.lower() == "s":

        print("\nOpciones:", opciones)

        jugada1 = input(f"{nombre1}: ").lower()
        jugada2 = input(f"{nombre2}: ").lower()

        # Operador lógico OR
        if jugada1 not in opciones or jugada2 not in opciones:
            print("Opción inválida.")
            continue

        resultado = determinar_ganador(jugada1, jugada2)

        if resultado == 0:
            print("Empate")

        elif resultado == 1:
            print(f"Gana {nombre1}")
            puntos1 += 1

        else:
            print(f"Gana {nombre2}")
            puntos2 += 1

        print(f"Marcador: {nombre1} {puntos1} - {puntos2} {nombre2}")

        continuar = input("¿Jugar otra ronda? (s/n): ")

    print("\nRESULTADO FINAL")
    print(f"{nombre1}: {puntos1}")
    print(f"{nombre2}: {puntos2}")


# -----------------------------------
# MODO VS SERVIDOR
# -----------------------------------
def jugar_servidor():

    print("\n=== MODO VS SERVIDOR ===")

    nombre = input("Ingrese su nombre: ")

    puntos_jugador = 0
    puntos_servidor = 0

    continuar = "s"

    while continuar.lower() == "s":

        print("\nOpciones:", opciones)

        jugador = input("Tu elección: ").lower()

        if jugador not in opciones:
            print("Opción inválida.")
            continue

        servidor = random.choice(opciones)

        print("Servidor eligió:", servidor)

        resultado = determinar_ganador(jugador, servidor)

        if resultado == 0:
            print("Empate")

        elif resultado == 1:
            print("¡Ganaste!")
            puntos_jugador += 1

        else:
            print("Gana el servidor")
            puntos_servidor += 1

        print(
            f"Marcador -> {nombre}: {puntos_jugador} | Servidor: {puntos_servidor}"
        )

        continuar = input("¿Jugar otra ronda? (s/n): ")

    print("\nRESULTADO FINAL")
    print(f"{nombre}: {puntos_jugador}")
    print(f"Servidor: {puntos_servidor}")


# -----------------------------------
# MENÚ PRINCIPAL
# -----------------------------------
def menu():

    while True:

        print("\n====================")
        print(" PIEDRA PAPEL TIJERA ")
        print("====================")
        print("1. Dos jugadores")
        print("2. Contra servidor")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        # Operadores relacionales y lógicos
        if opcion == "1":
            jugar_dos_jugadores()

        elif opcion == "2":
            jugar_servidor()

        elif opcion == "3":
            print("Programa finalizado.")
            break

        else:
            print("Opción incorrecta.")


# -----------------------------------
# INICIO DEL PROGRAMA
# -----------------------------------
menu()