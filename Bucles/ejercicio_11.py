"""
Enunciado:

#De los 3 Jugadores de un Reality Show, se registra:
#nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibió en la etapa de votos

#Informar:

#a. nombre del candidato con más votos
#b. nombre y edad del candidato con menos votos
#c. el promedio de edades de los candidatos
#d. total de votos emitidos.

#Todos los datos se ingresan mediante input()
"""

# Tomás Romero
# TP REALITY SHOW

contador_jugadores = 0
edad_total = 0
votos_totales = 0

while contador_jugadores < 3:

    nombre_jugador = input("Ingrese el nombre del jugador: ")
    
    edad_jugador = int(input("Ingrese la edad del jugador: "))
    while edad_jugador < 26:
        edad_jugador = int(input("Debe ser mayor a 25 años. Reingrese la edad: "))

    cantidad_votos = int(input("Ingrese la cantidad de votos: "))
    while cantidad_votos < 0:
        cantidad_votos = int(input("Los votos no pueden ser negativos. Reingrese la cantidad de votos: "))

    print("------------------------")

    if contador_jugadores == 0:
        votos_minimo = cantidad_votos
        votos_maximo = cantidad_votos
        jugador_mas_votado = nombre_jugador
        jugador_menos_votado = nombre_jugador
        edad_jugador_menos_votado = edad_jugador
    elif cantidad_votos > votos_maximo:
        jugador_mas_votado = nombre_jugador
        votos_maximo = cantidad_votos
    elif cantidad_votos < votos_minimo:
        jugador_menos_votado = nombre_jugador
        edad_jugador_menos_votado = edad_jugador
        votos_minimo = cantidad_votos
    
    edad_total += edad_jugador
    votos_totales += cantidad_votos

    contador_jugadores += 1

edad_promedio = edad_total / contador_jugadores

mensaje_resultados= f'''RESULTADOS:
a-El jugador mas votado es: {jugador_mas_votado}.
b-El jugador menos votado es: {jugador_menos_votado} de {edad_jugador_menos_votado} años.
c-El promedio de edad de los jugadores es de: {edad_promedio} años.
d-El total de votos emitidos es de: {votos_totales} votos.
Muchas gracias por participar en While_Reality_Show!!!
-----------------------'''

print(mensaje_resultados)
