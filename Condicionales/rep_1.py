# A partir del ingreso de la altura en centímetros de un jugador de baloncesto, el programa deberá determinar la posición del jugador en la cancha, considerando los siguientes parámetros:
#Menos de 160 cm: Base
#Entre 160 cm y 179 cm: Escolta
#Entre 180 cm y 199 cm: Alero
#200 cm o más: Ala-Pívot o Pívot

# Tomás Romero
# Condicionales Rojo 1

altura_ingresada =  input("Ingrese la altura: ")
altura_ingresada = int(altura_ingresada)

if altura_ingresada >= 200:
    print("Ala-Pívot o Pívot")
elif altura_ingresada < 160:
    print("Base")
elif altura_ingresada <= 179:
    print("Escolta")
else:
    print("Alero")
