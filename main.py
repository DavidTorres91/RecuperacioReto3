#Código principal donde se implementa la lógica del juego WorldCraftASCII.

import utilidades

print("Bienvenido jugador.")

CDIA = input("Cual es tu CDIA?")

print(utilidades.validar_CDIA(CDIA))