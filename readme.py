### ____________________________
#   WORLDCRAFT ASCII  
  ##############################

# IDENTIFICAR

Este reto se trata de implementar un programa que permita verificar los datos de un aspirante a jugador del juego y asignarle un nivel de inicio.

# DEFINIR

Esta función tiene como objetivo realizar una verificación para evaluar la posibilidad de que una persona pueda ingresar como nuevo jugador del WorldCraft ASCII, para ello se solicita el CDIA (código de identificación ASCII) del aspirante. Este CDIA es una cadena de 15 caracteres que debe cumplir con las siguientes restricciones y las cuales deben ser validadas por el programa una vez se ingresa:
+ Convertir el CDIA a minúsculas
+ El CDIA debe tener 4 dígitos numéricos
+ En la posición 8 de la cadena del CDIA debe ir siempre el carácter menos (‘-’)
+ El carácter en la segunda posición y el carácter de la penúltima posición del CDIA
deben ser diferentes.
+ El código CDIA no debe contener más de 1 vez la letra ’o’
+ El CDIA debe tener al menos uno de los siguientes símbolos (‘>’,’=’, ‘@’)

**Si el CDIA no cumple con alguna de estas reglas se debe presentar el mensaje “CDIA inválido”**

Una vez se ha validado el código CDIA se le deben hacer las siguientes preguntas:
+ Fecha de Nacimiento (en formato AAAA-MM-DD)
  + (la edad del jugador debe ser mayor a 15 años y debes calcularla)
+ Si la edad es correcta debes preguntar los siguientes datos
  + Alias del jugador (Una cadena de caracteres de una longitud máxima de 8 y
debe contener al menos un número)
  + Preguntar ¿Ya has jugado WorldCraft ASCII? (Si = 1, No = 0)
  + Si ya ha jugado asignar el nivel 10
  + Si no ha jugado asignar el nivel 1.
+ Si la edad del jugador es igual o inferior a 15 debe mostrar un mensaje que no puede jugar


Segundo sub-reto: Asignar mundo
Cuando un nuevo jugador es admitido al WorldCraft ASCII se le debe asignar un Mundo
para iniciar a jugar de acuerdo con las siguientes reglas:
+ Mundo 1: jugadores entre 16 y 30 años que no han jugado antes.
+ Mundo 2: jugadores entre 16 y 30 años que ya han jugado antes.
+ Mundo 3: jugadores entre 31 y 40 años que ya han jugado antes
+ Mundo 4: jugadores mayores a 40 años que no han jugado antes
El programa debe tener una función que reciba la edad (ya calculada) del nuevo jugador,
la respuesta si ha jugado antes, con estos datos debe retornar el mundo que le
corresponde al jugador.

# ALGORITMOS
