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
# Simulacro Match

salida = "Si"
contador_cartas_raras = 0
contador_cartas_super_raras = 0
contador_cartas_ultra_raras = 0
contador_cartas_ultra_raras_valiosas = 0
bandera_cartas_raras = 0
precio_total_magicas = 0
precio_total_monstruos = 0
precio_total_trampas = 0
contador_cartas_magicas = 0
contador_cartas_monstruos = 0
contador_cartas_trampas = 0


while salida == "Si":
    nombre_carta = input("Ingrese el nombre de la carta: ")
    precio_carta = float(input("Ingrese su precio: "))
    while precio_carta < 0:
        precio_carta = float(input("¡ATENCIPON! El valor no puede ser negativo.\nReingrese el precio: "))
    tipo_carta = input("Ingrese su tipo (Magica, Monstruo, Trampa):")
    while tipo_carta != "Magica" and tipo_carta != "Monstruo" and tipo_carta != "Trampa":
        tipo_carta = input("¡ATENCIÓN! Tipo de carta invalida.\nReingrese su tipo: ")
    rareza_carta = input("Ingrese su rareza: (Rara, Super Rara, Ultra Rara): ")
    while rareza_carta != "Rara" and rareza_carta != "Super Rara" and rareza_carta != "Ultra Rara":
        rareza_carta = input("¡ATENCIÓN! Rareza de carta invalida.\nReingrese su rareza: ")
    print("---------------------------")

    match rareza_carta:
        case "Rara":
            contador_cartas_raras += 1
            if bandera_cartas_raras == 0:
                nombre_carta_rara_menor_valor = nombre_carta
                precio_carta_rara_menor_valor = precio_carta
                tipo_carta_rara_menor_valor = tipo_carta
                bandera_cartas_raras = 1
            elif precio_carta < precio_carta_rara_menor_valor:
                nombre_carta_rara_menor_valor = nombre_carta
                precio_carta_rara_menor_valor = precio_carta
                tipo_carta_rara_menor_valor = tipo_carta

        case "Ultra Rara":
            contador_cartas_ultra_raras += 1
            if precio_carta > 49999 and precio_carta < 80001:
                contador_cartas_ultra_raras_valiosas +=1
            
        case _:
            contador_cartas_super_raras += 1

    match tipo_carta:
        case "Magica":
            precio_total_magicas += precio_carta
            contador_cartas_magicas += 1
        case "Monstruo":
            precio_total_monstruos += precio_carta
            contador_cartas_monstruos += 1
        case _:
            precio_total_trampas += precio_carta
            contador_cartas_trampas +=1
    
    salida = input("¿Desea ingresar una carta nueva? Si / No :")
    print("---------------------------")

total_cartas = contador_cartas_raras + contador_cartas_super_raras + contador_cartas_ultra_raras
promedio_cartas_raras = (contador_cartas_raras * 100) // total_cartas
promedio_cartas_super_raras = (contador_cartas_super_raras * 100) // total_cartas
promedio_cartas_ultra_raras = (contador_cartas_ultra_raras * 100) // total_cartas

if contador_cartas_magicas > 0:
    precio_promedio_magicas = precio_total_magicas // contador_cartas_magicas
else:
    precio_promedio_magicas = 0
if contador_cartas_monstruos > 0: 
    precio_promedio_monstruos = precio_total_monstruos // contador_cartas_monstruos
else:
    precio_promedio_monstruos = 0
if contador_cartas_trampas > 0:
    precio_promedio_trampas = precio_total_trampas // contador_cartas_trampas
else:
    precio_promedio_trampas = 0

if precio_total_magicas > precio_total_monstruos and precio_total_magicas > precio_total_trampas:
    tipo_carta_mas_vendida = "Magica"
elif precio_total_monstruos > precio_total_trampas:
    tipo_carta_mas_vendida = "Monstruo"
else:
    tipo_carta_mas_vendida = "Trampa"


mensaje_final = f'''
RESULTADOS:
A- Cantidad de cartas Ultra Raras entre $50.000 y $80.000: {contador_cartas_ultra_raras_valiosas}.
B- La carta Rara de menor valor fue "{nombre_carta_rara_menor_valor}" de tipo {tipo_carta_rara_menor_valor}.
C- Porcentaje segun rareza:
    Raras: {promedio_cartas_raras}%.
    Super Raras: {promedio_cartas_super_raras}%.
    Ultra Raras: {promedio_cartas_ultra_raras}%.
D- Precio promedio segun tipo:
    Magicas: ${precio_promedio_magicas}.
    Monstruos: ${precio_promedio_monstruos}.
    Trampa: ${precio_promedio_trampas}.
E- Tipo de carta mas vendida: {tipo_carta_mas_vendida}.    
'''

print(mensaje_final)
