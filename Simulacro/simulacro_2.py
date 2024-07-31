'''En una partida de todos contra todos de CS-GO (Juego de disparos) un grupo de 5 amigos quiere saber las estadísticas al finalizar la partida.
Para esto se requieren los siguientes datos:
Nombre del jugador.
Edad del jugador - Mayor de edad.
Bajas (Cantidad de veces que mató) - Número positivo inclusive 0.
Muertes (Cantidad de veces que murió) - Número positivo inclusive 0.

INFORMAR
A) Nombre del jugador más joven.
B) El jugador que más bajas tuvo.
C) El jugador que menos muertes tuvo.
D) El promedio de bajas.
E) Cantidad de jugadores que tienen entre 20 y 30 años cuyas bajas están entre 10 y 15.
F) El nombre y edad del jugador que más muertes tuvo.'''


contador = 0
bandera_contador = 0
contador_jugadores_veinteaneros = 0
contador_bajas_totales = 0


while contador < 5:
    nombre_jugador = input("Nombre del jugador: ")
    edad_jugador = int(input("Edad del jugador (+18): "))
    while edad_jugador < 18:
        edad_jugador = int(input("¡ATENCIÓN! Debe ser mayor de edad.\nReingrese la edad: "))
    bajas_jugador = int(input("Enemigos asesinados: "))
    while bajas_jugador < 0:
        bajas_jugador = int(input("¡ATENCIÓN! No se admiten valores negativos.\nReingrese el número de bajas: "))
    muertes_jugador = int(input("Veces que murio: "))
    while muertes_jugador < 0:
        muertes_jugador = int(input("¡ATENCIÓN! No se admiten valores negativos.\nReingrese el número de veces que murio: "))
    print("-----------------------------------------")

    if bandera_contador == 0:
        nombre_jugador_mas_joven = nombre_jugador
        edad_jugador_mas_joven = edad_jugador
        nombre_jugador_mas_muertes = nombre_jugador
        edad_jugador_mas_muertes = edad_jugador
        muertes_jugador_mas_muertes = muertes_jugador
        bandera_contador = 1

    if edad_jugador < edad_jugador_mas_joven:
        nombre_jugador_mas_joven = nombre_jugador
        edad_jugador_mas_joven = edad_jugador

    if muertes_jugador > muertes_jugador_mas_muertes:
        nombre_jugador_mas_muertes = nombre_jugador
        edad_jugador_mas_muertes = edad_jugador
        muertes_jugador_mas_muertes = muertes_jugador

    if edad_jugador > 19 and edad_jugador < 31 and bajas_jugador > 9 and bajas_jugador < 16:
        contador_jugadores_veinteaneros += 1


    contador_bajas_totales += bajas_jugador

    contador += 1
    

promedio_bajas = contador_bajas_totales / contador


mensaje_final = f'''
        RESULTADOS:
        A- El jugador mas joven es: {nombre_jugador_mas_joven}.
        B- El jugador con mas bajas es: 
        C- El jugadro con menos muertes es:
        D- El promedio de bajas es de {promedio_bajas}%.
        E- Jugadores entre 20 y 30 años y 10 y 15 bajas: {contador_jugadores_veinteaneros}.
        F- El jugador con mas muertes es {nombre_jugador_mas_muertes} de {edad_jugador_mas_muertes} años.
'''

print(mensaje_final)