#En este modulo agregar la función de validación del código CDIA

def buscar_CDIA(CDIA: str) -> bool:
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
	lista = ["juank@vv+=","carlo@v?+k","mario@kv=+"]

	if CDIA in lista:
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
	#  
	#------------------------------------------------
	# Escribir las validaciones

 

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
	# Devuelve el CDIA en minuscula
  
  return CDIA.lower()
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
  for i in CDIA[i]:
    if CDIA[i].isnumeric
      contador = contador +1
    
  #------------------------------------------------
	# Contiene 4 numeros?
	#------------------------------------------------
	# Si contador contiene 4 numeros devuelve True sino False 
    if contador == 4
      return True
    else
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
  if CDIA[8] == "-":
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
  if CDIA[2] == CDIA[-2]:
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
  if CDIA.count("o") >= 1:
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
  if CDIA.find("=") or CDIA.find("?") or CDIA.find("&") :
    return True
  else:
    return False 

  
