#Realizar un programa que a partir del ingreso de un sueldo y de un porcentaje de aumento, calcule y muestre el sueldo con el aumento porcentual 
# ingresado por el usuario.

# Tomás Romero
# E/S 8

sueldo_ingresado = input("Ingrese su sueldo: ")
porcentaje_ingresado = input("Ingrese el porcetanje que quiere aumentar: ")

sueldo_ingresado = float (sueldo_ingresado)
porcentaje_ingresado = float(porcentaje_ingresado)

aumento = sueldo_ingresado * porcentaje_ingresado/100

sueldo_aumentado = sueldo_ingresado + aumento

print(f"El sueldo original era de {sueldo_ingresado} y el sueldo con el aumento del {porcentaje_ingresado}% es de {sueldo_aumentado}")