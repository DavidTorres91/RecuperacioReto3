#Código principal donde se implementa la lógica del juego WorldCraftASCII.
import os
import utilidades
NuevReg=True
centinela=None
edad=0
while NuevReg==True:
  while centinela==None:
    print(utilidades.titulo)
    print("""*******************
|Cual es tu CDIA? | 
*******************\n""")
    CDIA = input()
    os.system ("clear") 
    if utilidades.validar_CDIA(CDIA):
      utilidades.validar_CDIA(CDIA)
      centinela=True
    else:
      print("Ingrese un valor Valido")
  centinela=None
  while centinela==None:
    try:
      print(utilidades.titulo)
      print("""***********************************************
|Cual es tu fecha de nacimeinto? (DD,MM,YYYY) | 
***********************************************\n""")
      fecha = input()
      os.system ("clear") 
      if utilidades.edad(fecha):
        utilidades.edad(fecha)
        centinela=True
    except(ValueError):
      print("Ingrese una fecha valida")
  edad=utilidades.edad(fecha)
  centinela=None
  while centinela==None:
    print(utilidades.titulo)
    print("""*******************
|Cual es tu Alias?|
*******************\n""")
    alias = input()
    os.system ("clear") 
    if utilidades.val_alias(alias):
      utilidades.val_alias(alias)
      centinela=True
    else:
      print("Ingrese un Alias Valido")
  centinela=None
  while centinela==None:
  
    print(utilidades.titulo)
    print("""***************************************************
|Ya has jugado WorldCraftASCII antes? (Si=1,No=0)| 
***************************************************\n""")
    antiguo = input()
    os.system ("clear") 
    if antiguo=="1" or antiguo=="0":
      utilidades.asignar_nivel(int(antiguo))
      centinela=True
    else:
      print("Ingrese un valor valida")
  
  print(utilidades.resumen(CDIA,alias,antiguo,edad))
  newreg = int(input("Desea agregar un nuevo registro?(Si=1,No=0) \n"))
  if newreg==1:
    centinela=None
    NuevReg=True
    os.system ("clear") 
  else:
    NuevReg=False