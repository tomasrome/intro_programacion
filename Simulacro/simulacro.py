'''El dueño de una tienda dedicada a la compra/venta de cartas de Yu-Gi-Oh, 
Desea ingresar en el sistema las ventas realizadas en el dia de la fecha y conocer 
ciertos datos en base a las cartas que se vendieron.

Deberemos desarrollar un sistema para que el dueño pueda ingresar la siguiente información hasta que el decida.

Nombre de carta
Precio (no puede ser menor a 0)
Tipo (Magica, Monstruo, Trampa)
Rareza (Rara, Super Rara, Ultra Rara)

A) Cantidad de cartas de rareza Ultra raras cuyo precio oscile en 50000 y 80000
B) El nombre y tipo de la carta con menor precio de la rareza Rara.
C) El porcentaje de rara, super rara y ultra rara hay sobre el total
[ej: 30% rara ,30% super rara, 40% ultra rara ( debe sumar 100)]
D) Determinar el precio promedio por cada tipo de carta
E) Determinar cual fue el tipo de carta mas vendida
'''

# Tomás Romero
# Simulacro

contador_while = 0
contador_cartas_raras = 0
salida = "Si"

while salida == "Si":
    nombre_carta = input("-Ingrese el nombre de la carta: ")
    precio_carta = float(input("-Ingrese su precio: "))
    while precio_carta < 0:
        precio_carta = float(input("¡ATENCIÓN! El precio no puede ser negativo.\n Ingrese su precio: "))
    tipo_carta = input("-Ingrese su tipo (Magica, Monstruo, Trampa): ")
    while tipo_carta != "Magica" and tipo_carta != "Monstruo" and tipo_carta != "Trampa":
        tipo_carta = input("¡ATENCIÓN! Tipo de carta invalido.\n Ingrese su tipo: ")
    rareza_carta = input("-Ingrese su rareza (Rara, Super Rara, Ultra Rara): ")
    while rareza_carta != "Rara" and rareza_carta != "Super Rara" and rareza_carta != "Ultra Rara":
        rareza_carta = input("¡ATENCIÓN! Rareza de carta invalida.\n Ingrese su rareza: ")
    print("-------------------")
    salida = input("¿Desea cargar otra carta? Si / No: ")
    print("-------------------")
    
    if contador_while == 0:
        cantidad_cartas_raras = 0
        cantidad_cartas_super_raras = 0
        cantidad_cartas_ultra_raras = 0
        precio_total_magica = 0
        precio_total_monstruo = 0
        precio_total_trampa = 0
        cantidad_cartas_magicas = 0
        cantidad_cartas_monstruo = 0
        cantidad_cartas_trampa = 0
        contador_ultra_raras_valiosas = 0
    
    if rareza_carta == "Rara":
        cantidad_cartas_raras += 1
        if contador_cartas_raras == 0:
            nombre_rara_menor_precio = nombre_carta
            tipo_rara_menor_precio = tipo_carta
            carta_rara_menor_precio = precio_carta
            contador_cartas_raras += 1
        elif precio_carta < carta_rara_menor_precio:
            nombre_rara_menor_precio = nombre_carta
            tipo_rara_menor_precio = tipo_carta
            carta_rara_menor_precio = precio_carta
        
    elif rareza_carta == "Super Rara":
        cantidad_cartas_super_raras += 1
    else:
        cantidad_cartas_ultra_raras += 1
        if precio_carta > 49999 and precio_carta < 80001:
            contador_ultra_raras_valiosas += 1

    if tipo_carta == "Magica":
        cantidad_cartas_magicas += 1
        precio_total_magica += precio_carta
    elif tipo_carta == "Monstruo":
        cantidad_cartas_monstruo += 1
        precio_total_monstruo += precio_carta
    else:
        cantidad_cartas_trampa += 1
        precio_total_trampa += precio_carta

    contador_while += 1

total_cartas = cantidad_cartas_raras + cantidad_cartas_super_raras + cantidad_cartas_ultra_raras
promedio_cartas_raras = (cantidad_cartas_raras * 100) // total_cartas
promedio_cartas_super_raras = (cantidad_cartas_super_raras * 100) // total_cartas
promedio_cartas_ultra_raras = (cantidad_cartas_ultra_raras * 100) // total_cartas

precio_promedio_magica = precio_total_magica // cantidad_cartas_magicas
precio_promedio_monstruo = precio_total_monstruo // cantidad_cartas_monstruo
precio_promedio_trampa = precio_total_trampa // cantidad_cartas_trampa

cantidad_carta_mas_vendida = cantidad_cartas_magicas
if cantidad_carta_mas_vendida < cantidad_cartas_monstruo:
    if cantidad_cartas_monstruo > cantidad_cartas_trampa:
        carta_mas_vendida = "Monstruo"
    else:
        carta_mas_vendida = "Trampa"      
elif cantidad_carta_mas_vendida < cantidad_cartas_trampa:
        carta_mas_vendida = "Trampa"
else:
    carta_mas_vendida = "Magica"

mensaje_final = f'''------------------
RESULTADOS:
A- Cantidad de cartas de rareza Ultra Raras con precio entre $50.000 y $80.000: {contador_ultra_raras_valiosas} cartas.
B- La carta Rara de menor precio fue : {nombre_rara_menor_precio} de tipo {tipo_rara_menor_precio}
C- Promedio de cartas:
    Raras: {promedio_cartas_raras}%
    Super Raras: {promedio_cartas_super_raras}%
    Ultra Raras: {promedio_cartas_ultra_raras}%
D- Precio promedio por tipo:
    Magicas: ${precio_promedio_magica}
    Monstruo: ${precio_promedio_monstruo}
    Trampa: ${precio_promedio_trampa}
E- Tipo de carta mas vendida: {carta_mas_vendida}

'''
print(mensaje_final)

