'''
UTN Inversiones, realiza un estudio de mercado para saber cuál será la nueva
franquicia que se insertará en el mercado argentino y en la cual invertirán.
Las posibles franquicias son las siguientes: Apple, Dunkin o Ikea.
Para ello, se realizará una encuesta mediante un sistema de voto electrónico, con el
propósito de conocer cuáles son los gustos de los encuestados (no se sabe cuántos):
Se ingresa de cada encuestado:
● nombre
● edad (no menor a 18)
● está empleado (si-no)
● género (Masculino - Femenino - Otro)
● voto (APPLE, DUNKIN, IKEA)
Se necesita saber:
1. Cantidad de encuestados empleados que votaron por IKEA o APPLE, cuya
edad no supere los 36 años.
2. Nombre y voto del encuestado de género Femenino con mayor edad.
3. Porcentaje de encuestados de género Otro que votaron por DUNKIN.
4. Edad promedio de cada género.
5. Determinar cuál fue el género que tuvo menos encuestados.
'''
# TEMA B -T M-P- Enunciado-Apellidos[K-R]
# Tomás Romero - Div. 105


salida = "Si"
contador_total_encuestados = 0
contador_genero_masculino = 0
contador_genero_femenino = 0
contador_genero_otro = 0
contador_empleados_apple_ikea = 0
contador_genero_otro_dunkin = 0
total_edad_masculino = 0
total_edad_femenino = 0
total_edad_otro = 0
bandera_femenino = 0

while salida == "Si" or salida == "si":
    nombre_encuestado = input("Ingrese su nombre: ")
    edad_encuestado = int(input("Ingrese se edad (+18): "))
    while edad_encuestado < 18:
        edad_encuestado = int(input("¡ATENCIÓN! Debe ser mayor de edad.\nReingrese su edad: "))
    empleado_encuestado = input("¿Está empleado? (si - no): ")
    while empleado_encuestado != "si" and empleado_encuestado != "no":
        empleado_encuestado = input("¡ATENCIÓN! Valor ivalido.\n Reingrese su respuesta: ")
    genero_encuestado = input("Ingrese su genero (Masculino - Femenino - Otro): ")
    while genero_encuestado != "Masculino" and genero_encuestado != "Femenino" and genero_encuestado != "Otro":
        genero_encuestado = input("¡ATENCIÓN! Valor ivalido.\n Reingrese su genero: ")
    voto_encuestado = input("Ingrese su voto (APPLE, DUNKIN, IKEA): ")
    while voto_encuestado != "APPLE" and voto_encuestado != "DUNKIN" and voto_encuestado != "IKEA":
        voto_encuestado = input("¡ATENCIÓN! Valor ivalido.\n Reingrese su voto: ")
    print("---------------------------")

    match genero_encuestado:
        case "Masculino":
            contador_genero_masculino += 1
            total_edad_masculino += edad_encuestado
        case "Femenino": # 2- Nombre y voto del encuestado de género Femenino con mayor edad.
            if bandera_femenino == 0:
                nombre_femenino_mayor_edad = nombre_encuestado
                voto_femenino_mayor_edad = voto_encuestado
                edad_femenino_mayor_edad = edad_encuestado
                bandera_femenino = 1
            elif edad_encuestado > edad_femenino_mayor_edad:
                nombre_femenino_mayor_edad = nombre_encuestado
                voto_femenino_mayor_edad = voto_encuestado
                edad_femenino_mayor_edad = edad_encuestado
            contador_genero_femenino += 1
            total_edad_femenino += edad_encuestado
        case _: # 3- Porcentaje de encuestados de género Otro que votaron por DUNKIN.
            if voto_encuestado == "DUNKIN": 
                contador_genero_otro_dunkin += 1
            contador_genero_otro += 1
            total_edad_otro  += edad_encuestado

# 1- Cantidad de encuestados empleados que votaron por IKEA o APPLE, cuya edad no supere los 36 años.
    if empleado_encuestado == "si" and edad_encuestado < 36:
        if voto_encuestado == "IKEA" or voto_encuestado == "APPLE":
            contador_empleados_apple_ikea += 1
        
    contador_total_encuestados += 1
    salida = input("¿Desea ingresar otro encuestado? Si - No: ")


# 3- Porcentaje de encuestados de género Otro que votaron por DUNKIN.
porcentaje_genero_otro_dunkin = (contador_genero_otro_dunkin * 100) // contador_total_encuestados

# 4- Edad promedio de cada género.
if contador_genero_masculino != 0:
    edad_promedio_masculino = total_edad_masculino // contador_genero_masculino
else:
    edad_promedio_masculino = 0
if contador_genero_femenino != 0:
    edad_promedio_femenino = total_edad_femenino // contador_genero_femenino
else:
    edad_promedio_femenino = 0
if contador_genero_otro != 0:
    edad_promedio_otro = total_edad_otro // contador_genero_otro
else:
    edad_promedio_otro = 0

# 5- Determinar cuál fue el género que tuvo menos encuestados.
if contador_genero_masculino < contador_genero_femenino and contador_genero_masculino < contador_genero_otro:
    genero_menos_encuestados = "Masculino"
elif contador_genero_femenino < contador_genero_otro:
    genero_menos_encuestados = "Femenino"
else:
    genero_menos_encuestados = "Otro"

# 2- Definimos el mensaje dependiendo de si se ingreso o no un encuestado de genero Femenino.
if contador_genero_femenino != 0:
    mensaje_femenino_mayor_edad = f"{nombre_femenino_mayor_edad} y su voto fue para {voto_femenino_mayor_edad}."
else:
    mensaje_femenino_mayor_edad = "No se ingreso ningun encuestado de genero Femenino."


mensaje_final = f'''
RESULTADOS:
1- Cantidad de encuestados empleados que votaron por IKEA o APPLE, cuya edad no supere los 36 años: {contador_empleados_apple_ikea} encuestados.
2- Nombre y voto del encuestado de género Femenino con mayor edad: {mensaje_femenino_mayor_edad}
3- Porcentaje de encuestados de género Otro que votaron por DUNKIN: {porcentaje_genero_otro_dunkin}%.
4- Edad promedio de cada género:
    - Masculino: {edad_promedio_masculino} años.
    - Femenino: {edad_promedio_femenino} años.
    - Otro: {edad_promedio_otro} años.
5- Género que tuvo menos encuestados: {genero_menos_encuestados}.
'''

print(mensaje_final)