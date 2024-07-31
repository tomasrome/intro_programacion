"""
Se realiza un estudio de mercado para determinar cuál será la nueva franquicia 
que se insertará en el mercado argentino y en la cual invertirán.
Las posibles franquicias son las siguientes:
    STARBUCKS
    Zara
    MCDONALDS
    Bershka
    KFC

Para ello, se realizará una encuesta mediante un sistema de voto electrónico, 
con el propósito de conocer cuáles son los gustos de los encuestados.

Datos a ingresar:
    Nombre del encuestado
    Edad (no menor a 18)
    Género (Masculino - Femenino - Otro)
    Voto (STARBUCKS, MCDONALDS, ZARA, KFC)
    Situación Laboral (Empleado - Desempleado)


Consignas:
    a-Nombre y situación laboral de la persona con mayor edad que voto por Zara.
    b-Nombre y voto de la persona de sexo Otro de entre 60 y 70 años.
    c-Cantidad de encuestados desempleados que votaron por Starbucks, cuya edad esté entre 30 y 45 años inclusive.
    d-Quien de todos los sexos fue el que mas votó por Zara.
"""


seguir = "si"
bandera_zara = 0
contador_desempleados_starbucks = 0
contador_masculino = 0
contador_femenino = 0
contador_otros = 0

while seguir == "si":

    nombre_encuestado = input("Ingrese su nombre: ")
    edad_encuestado = int(input("Ingrese su edad (+18): "))
    while edad_encuestado < 18:
        edad_encuestado = int(input("¡ATENCIÓN! Dede ser mayor de edad.\nReingrese su edad :"))
    genero_encuestado = input("Ingrese su genero (Masculino - Femenino - Otro): ")
    while genero_encuestado != "Masculino" and genero_encuestado != "Femenino" and genero_encuestado != "Otro":
        genero_encuestado = input("¡ATENCIÓN! Genero invalido.\nReingrese su genero :")
    voto_encuestado = input("Ingrese su voto (STARBUCKS, MCDONALDS, ZARA, KFC, BERSHKA): ")
    while voto_encuestado != "STARBUCKS" and voto_encuestado != "MCDONALDS" and voto_encuestado != "ZARA" and voto_encuestado != "BERSHKA":
        voto_encuestado = input("¡ATENCIÓN! Voto invalido.\nReingrese su voto :")
    situacion_laboral_empleado = input("Ingrese su situacion laboral (Empleado - Desempleado): ")
    while situacion_laboral_empleado != "Empleado" and situacion_laboral_empleado != "Desempleado":
        voto_encuestado = input("¡ATENCIÓN! Valor invalido.\nReingrese su situación laboral :")
    print("---------------------------------------")

    match voto_encuestado:

        case "STARBUCKS":
            if situacion_laboral_empleado == "Desempleado" and edad_encuestado > 29 and edad_encuestado < 46:
                contador_desempleados_starbucks += 1
            
        case "ZARA":
            if bandera_zara == 0:
                nombre_persona_mayor_edad = nombre_encuestado
                situacion_laboral_persona_mayor_edad = situacion_laboral_empleado
                edad_persona_mayor_edad = edad_encuestado
            elif edad_encuestado > edad_persona_mayor_edad:
                nombre_persona_mayor_edad = nombre_encuestado
                situacion_laboral_persona_mayor_edad = situacion_laboral_empleado

            match genero_encuestado:
                case "Femenino":
                    contador_femenino += 1
                case "Masculino":
                    contador_masculino += 1
                case _:
                    contador_otros += 1
                

    salida = input("¿Desea continuar? Si / No")