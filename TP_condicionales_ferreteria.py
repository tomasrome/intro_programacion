#TP Condicionales:
#Ferrete Lámparas

#En una ferretería se quiere implementar un sistema que permita a los usuarios saber cuánto deberán pagar por la compra de lámparas de bajo consumo. Se tiene en cuenta que todas las lámparas cuestan $800.

#Se aplicará el siguiente descuento:
#Si compra 6 o más  lámparas bajo consumo tiene un descuento del 50%. 
#Si compra 5  lámparas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
#Si compra 4  lámparas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
#Si compra 3  lámparas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.

#Por otro lado, si el importe final con descuento suma más de $4000  se obtiene un descuento adicional de 5%.

#Mostrar por pantalla: 

#Marca, cantidad de lámparas, total a pagar sin descuento, el descuento obtenido si corresponde, el descuento adicional (si corresponde) y el total a pagar con descuento.

precio_lamparas = 800
cantidad_lamparas = input("Ingrese la cantidad de lamparas: ")
cantidad_lamparas = int(cantidad_lamparas)
marca_lamparas = input("Ingrese la marca de la lampara: ")
descuento = 0

if cantidad_lamparas > 5:
    descuento = 50
elif cantidad_lamparas == 5:
    if marca_lamparas == "ArgentinaLuz":
        descuento = 40
    else:
        descuento = 30
elif cantidad_lamparas == 4:
    if marca_lamparas == "ArgentinaLuz" or marca_lamparas == "FelipeLamparas":
        descuento = 25
    else:
        descuento = 20
elif cantidad_lamparas == 3:
    if marca_lamparas == "ArgentinaLuz":
        descuento = 15
    elif marca_lamparas == "FelipeLamparas":
        descuento = 10
    else:
        descuento = 5

total_sin_descuento = cantidad_lamparas * precio_lamparas
descuento = total_sin_descuento * descuento/100
total_con_descuento = total_sin_descuento - descuento

print("--------------------------")
print(f"Marca: {marca_lamparas}.")
print(f"Cantidad de lamparas: {cantidad_lamparas}.")
print(f"Total sin descuento: ${total_sin_descuento}")
print(f"Descuento: ${descuento}")
if total_con_descuento > 4000:
    total_con_descuento = total_con_descuento - total_con_descuento*5/100
    print(f"Descuento adicional: 5%")
print(f"Total a pagar con descuento: ${total_con_descuento}")

