#Código principal donde se implementa la lógica del juego WorldCraftASCII.

import utilidades

print("Bienvenido jugador.")

CDIA = input("Cual es tu CDIA? \n")

print(utilidades.validar_CDIA(CDIA))

print(utilidades.buscar_CDIA(CDIA) , utilidades.validar_longitud_CDIA(CDIA) , utilidades.convertMin(CDIA) , utilidades.cont4num(CDIA) , utilidades.posicion_8_es_raya(CDIA) , utilidades.segundo_penultimo(CDIA) , utilidades.count_o(CDIA) , utilidades.almenos(CDIA) )
