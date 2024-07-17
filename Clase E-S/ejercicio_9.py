#Realizar un programa que a partir del ingreso del importe de una compra, aplique un 25% de descuento. Mostrar por pantalla 
# cuánto es el total a pagar y cuánto fue el descuento obtenido.

# Tomás Romero
# E/S 9

importe_ingresado = input("Ingrese el importe de la compra: ")

importe_ingresado = float(importe_ingresado)

descuento = importe_ingresado * 25/100
total_descuento = importe_ingresado - descuento

mensaje = f"Con el 25% de descuento el total a pagar es de {total_descuento}$ y el descuento fue de {descuento}$."

print(mensaje)  