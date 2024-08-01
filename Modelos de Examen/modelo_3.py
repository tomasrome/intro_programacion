"""

Se realiza un estudio de mercado para determinar cuál será la nueva franquicia 
que se insertará en el mercado argentino y en la cual invertirán.
Las posibles franquicias son las siguientes:
    The north face
    Zara
    Bershka

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
primer_voto_zara = 0 
cantidad_desempleados_starbucks = 0 
seguir = 'Si'
contador_zara_masculino = 0
contador_zara_femenino = 0
contador_zara_otro = 0
while seguir == 'Si':
    nombre = input('Ingrese su Nombre: ') 
  
    edad = input('Ingrese su edad: ')
    edad = int(edad)
    while edad < 18:
        edad = input('Reingrese su edad: ')
        edad = int(edad)
    
    genero_ingresado = input('Ingrese su genero: ')
    while genero_ingresado != 'Masculino' and genero_ingresado != 'Femenino' and genero_ingresado != 'Otro':
        genero_ingresado = input('Opcion no valida, Reingrese su genero: ')
    
    voto_ingresado = input('Ingrese a que empresa vota, las opciones son: "STARBUCKS", "MCDONALDS, "ZARA", "KFC" ')
    while voto_ingresado != "STARBUCKS" and voto_ingresado != "MCDONALDS" and voto_ingresado != "ZARA" and voto_ingresado != "KFC" and voto_ingresado != "BERSHKA":
        voto_ingresado = input('Reingrese a que empresa vota, las opciones son: "STARBUCKS", "MCDONALDS", "ZARA", "KFC" "Bershka"')
        
    situacion_laboral = input('Ingrese su situacion laboral (Empleado - Desempleado): ')
    while situacion_laboral != 'Empleado' and situacion_laboral != 'Desempleado':
        situacion_laboral = input('Reingrese su situacion laboral (Empleado - Desempleado): ')
    #A
    if voto_ingresado == "ZARA":
        if primer_voto_zara == 0:
            edad_votante_zara = edad
            nombre_votante_zara = nombre
            situacion_laboral_zara = situacion_laboral
            primer_voto_zara = 1
        elif edad > edad_votante_zara:
            edad_votante_zara = edad
            nombre_votante_zara = nombre
            situacion_laboral_zara = situacion_laboral
        if genero_ingresado == "Masculino":#D
            contador_zara_masculino += 1
        elif genero_ingresado == "Femenino":
            contador_zara_femenino += 1
        else: 
            contador_zara_otro += 1
    #B
    if genero_ingresado == "Otro":
        if edad > 60 and edad < 70:
            nombre_genero_otro = nombre
            voto_genero_otro = voto_ingresado
    #C
    if situacion_laboral == "Desempleado":
        if voto_ingresado == "STARBUCKS":
            if edad > 30 and edad <= 45:
                cantidad_desempleados_starbucks += 1
   
    seguir = input('Desea seguir? Si - No: ')
