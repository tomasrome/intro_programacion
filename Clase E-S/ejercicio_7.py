# Realizar un programa que a partir del ingreso de un sueldo (valor flotante) muestre dicho valor con un incremento del 15%.

# Tomas Romero
# E/S 7

sueldo_ingresado = input("Ingrese su sueldo: ")

sueldo_ingresado = float (sueldo_ingresado)

aumento = sueldo_ingresado * 15/100

sueldo_aumentado = sueldo_ingresado + aumento

print(f"El sueldo original era {sueldo_ingresado} y el sueldo con el aumento es de {sueldo_aumentado}")