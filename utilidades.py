from datetime import datetime
import os,re

#En este modulo agregar la función de validación del código CDIA
titulo = ("""_____________________________________________
|                                           |
|    █░█░█ █▀█ █▀█ █░░ █▀▄ █▀▀ █▀█ ▄▀█ █▀▀  |
|    ▀▄▀▄▀ █▄█ █▀▄ █▄▄ █▄▀ █▄▄ █▀▄ █▀█ █▀░  |
|                                           |
|             ▄▀█ █▀ █▀▀ █ █                |
|             █▀█ ▄█ █▄▄ █ █                |
--------------------------------------------- """)

def buscar_CDIA(CDIA: str, ) -> bool:
  """ 
	Función encarga de validar si existe un código de CDIA registrado por un jugador

	Parameters
	-----------------
	CDIA : str
		Código de identificación ASCII

	Returns
	------------------
	existe : bool
		Retorna True si existe, de lo contrario False
	"""
  #Lista de usuarios CDIA
  global lista
  lista = ["juank@vv+=","carlo@v?+k","juank@v-1=!154P"]

  if CDIA in lista:
    return True

  else:
    return False


def validar_longitud_CDIA(CDIA: str) -> bool:
  """ 
	Función encarga de validar si un código de CDIA cumple con 15 caracteres de longitud

	Parameters
	-----------------
	CDIA : str
		Código de identificación ASCII

	Returns
	------------------
	existe : bool
		Retorna True si cumple, de lo contrario False
	"""
	#------------------------------------------------
	# CDIA contiene 15 caracteres?
	#------------------------------------------------
	# Si la longitud del CDIA es 15 
  if len(CDIA)==15:
	  return True
  else:
    return False

def convertMin(CDIA: str) -> str:
  """ 
	Función encarga de convertir un código de CDIA a minusculas

	Parameters
	-----------------
	CDIA : str
		Código de identificación ASCII

	Returns
	------------------
	CDIA : str
		Código de identificación ASCII en minuscula
	"""
	#------------------------------------------------
	# Convertir a minuscula. 
	#------------------------------------------------
	# Devuelve True des pues de convertir el CDIA en minuscula
  min = ""
  for i in range(0,len(CDIA)):
    min += CDIA[i].lower()
  return min 

def cont4num(CDIA: str) -> bool:
  """ 
	Función encarga de validar si un código de CDIA contiene 4 digitos numericos.

	Parameters
	-----------------
	CDIA : str
		Código de identificación ASCII

	Returns
	------------------
	existe : bool
		Retorna True si cumple, de lo contrario False
	"""
  #------------------------------------------------
	#  Contar numeros
	#------------------------------------------------
	# Un contador inicia en cero y se incrementa cada ves que una letra de CDIA es numerica. Luego si el contador es cuatro devuelve True sino False 

  contador = 0
  for i in range(0,len(CDIA)-1):
    if CDIA[i].isnumeric():
      contador = contador+1
  #------------------------------------------------
	# Contiene 4 numeros?
	#------------------------------------------------
	# Si contador contiene 4 numeros devuelve True sino False 
  if contador == 4:
    return True
  else:
    return False
def posicion_8_es_raya(CDIA: str) -> bool:
  """ 
	Función encarga de validar si un código de CDIA contiene - en la posicion 8.

	Parameters
	-----------------
	CDIA : str
		Código de identificación ASCII

	Returns
	------------------
	existe : bool
		Retorna True si cumple, de lo contrario False
	"""
  #------------------------------------------------
	#  Validar 8va posicion 
	#------------------------------------------------
	#  Si CDIA en la 8 posicion es "-"
  if CDIA[7] == "-":
    return True
  else:
    return False 

def segundo_penultimo(CDIA: str) -> bool:
  """ 
	Función encarga de validar si un código de CDIA contiene la segunda pocicion y la penultima son diferentes

	Parameters
	-----------------
	CDIA : str
		Código de identificación ASCII

	Returns
	------------------
	existe : bool
		Retorna True si cumple, de lo contrario False
	"""
  #------------------------------------------------
	#  Compara el segundo y el penultimo son diferentes   
	#------------------------------------------------
	# Si el segundo elemento de CDIA es diferentes al penultimo devuelva TRUE de lo contrario False
  if CDIA[1] != CDIA[-2]:
    return True
  else:
    return False 
    
def count_o(CDIA: str) -> bool:
  """ 
	Función encarga de validar si un código de CDIA no contiene "o" mas de una vez.
	Parameters
	-----------------
	CDIA : str
		Código de identificación ASCII

	Returns
	------------------
	existe : bool
		Retorna True si cumple, de lo contrario False
	"""
  #------------------------------------------------
	#  Compara el segundo y el penultimo son iguales   
	#------------------------------------------------
	# 
  plat=convertMin(CDIA)
  if plat.count("o")<=1:
    return True
  else:
    return False 

def almenos(CDIA: str) -> bool:
  """ 
	Función encarga de validar si un código de CDIA contiene "=" o ">" o "@".
	Parameters
	-----------------
	CDIA : str
		Código de identificación ASCII

	Returns
	------------------
	existe : bool
		Retorna True si cumple, de lo contrario False
	"""
  #------------------------------------------------
	#  Contiene "=" o ">" o "@"
	#------------------------------------------------
	# Revisar si contiene "=" o ">" o "@".
  if CDIA.find("=") or CDIA.find("?") or CDIA.find("&"):
    return True
  else:
    return False 

def validar_CDIA(CDIA: str) -> bool:
  """ 
	Función encarga de validar si existe un código de CDIA cumple las restricciones

	Parameters
	-----------------
	CDIA : str
		Código de identificación ASCII

	Returns
	------------------
	existe : bool
		Retorna True si cumple, de lo contrario False
	"""
	#------------------------------------------------
	#  Validar
	#------------------------------------------------
	# Si cumple las restricciones devuelve True sino False

  if(buscar_CDIA(CDIA)== False and validar_longitud_CDIA(CDIA) and convertMin(CDIA).islower() and cont4num(CDIA) and posicion_8_es_raya(CDIA) and segundo_penultimo(CDIA) and count_o(CDIA) and almenos(CDIA)):
    return True
  else:
    return False

def edad(fecha:str) -> int:
  """ 
	Función encarga de calcular la edad del usuario.

	Parameters
	-----------------
	fecha: str
		La fecha ingresada por el usuario como String.

	Returns
	------------------
	edad: int
		Retorna la edad en años del usuario
	"""
	#------------------------------------------------
	#  edad
	#------------------------------------------------
	# 1. En fecha1 transforma fecha de str a time.
  # 2. Calcula edad restando el año actual con el digitado por el usuario.
  # 3. Retorna edad.
  fecha1 = datetime.strptime(fecha, '%d/%m/%Y')
  edad=int(datetime.today().strftime("%Y"))-int(fecha1.strftime("%Y")) 
  return edad

def fechaN(fecha:str) -> bool:
  """ 
	Función encarga de validar si el usuario tiene por lo menos de 15 años

	Parameters
	-----------------
	fecha: str
		La fecha ingresada por el usuario como String.

	Returns
	------------------
	edad: bool
		Retorna True si cumple, de lo contrario False
	"""
	#------------------------------------------------
	#  Es mayor de 15?
	#------------------------------------------------
	# compara si la funcion edad devuelve un numero mayor a 15 y retorna True si cumple sino False
  if edad(fecha)>=15:
    return True
  else:
    return False

def val_alias(alias:str) -> bool:
  """ 
	Función encarga de validar si el usuario tiene un alias que cumple con ser maximo de 8 caracteres y tener 1 numero

	Parameters
	-----------------
	alias:str
		El alias ingresada por el usuario como String.

	Returns
	------------------
	alias_valido : bool
		Retorna True si cumple, de lo contrario False
	"""
	#------------------------------------------------
	#  Es alias cumple?
	#------------------------------------------------
	# compara si la logitud de alias en menor o igual a 8 y si es alfanumerico, esdecir que contenga almenos un numero y letras
  if len(alias) <= 8 and re.search(r'\d', alias):
    return True
  else:
    return False
    
def asignar_nivel(antiguo:int) ->int:
  """ 
	Función encarga de asignar el nivel de dificultad con el que iniciara el jugador

	Parameters
	-----------------
	antiguo:int
		Variable que determina si el jugador es antiguo.

	Returns
	------------------
	nivel: int
		Retorna el nivel segun; si es antiguo al nivel 10, sino al nivel 1. 
	"""
	#------------------------------------------------
	#Su nivel es:
	#------------------------------------------------
	# Compara si el jugador es antiguo y le asigna el nivel 10 de lo contrario asigna el nivel 1
  if int(antiguo) == 1:
    nivel=10
  else:
    nivel=1
  return nivel    

def seleccionador_de_mundo(edad:int, antiguo:int):
  """ 
	Función encarga de asignar el mundo donde iniciara el jugador

	Parameters
	-----------------
	edad,antiguo:int
		La edad del jugador y si es antiguo.

	Returns
	------------------
	mundo : int
		Retorna mundo
	"""
	#------------------------------------------------
	#Su mundo es:
	#------------------------------------------------
	# Compara si la edad del jugador esta en cierto rango y mira si es antiguo, segun estos parametros asigna el mundo.
  if edad >= 16 and edad <= 30 and int(antiguo) == 0:
    mundo = 1
  elif edad >= 16 and edad <= 30 and int(antiguo) == 1:
    mundo = 2
  elif edad >= 31 and edad <= 40 and int(antiguo) == 1:
    mundo = 3
  elif edad > 40 and int(antiguo) == 0:
    mundo = 4
  else:
    mundo=5
  return mundo


def resumen(CDIA:str,nickname:str,antiguo:int,edad:int):
  """ 
	Función encarga de pintar en pantalla el recumen de los datos del jugador

	Parameters
	-----------------
  CDIA,nickname: str
	edad,antiguo: int
		La edad del jugador y si es antiguo.

	Returns
	------------------
  Registro exitoso.
	"""
	#------------------------------------------------
	# Resumen:
	#------------------------------------------------
	# Limpia la pantalla, pone la informacion del usuario en pantalla
  os.system ("clear")
  print(titulo)
  print(f"""  + CDIA es: {CDIA}.
  + Alias es: {nickname}.
  + Nivel inicial: {asignar_nivel(antiguo)}.
  + Mundo inicial: {seleccionador_de_mundo(edad,antiguo)}.
  + Edad: {edad}.
  *****************************************""")
  lista.append(CDIA)
  return(print("Registro exitoso."))