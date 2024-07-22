# Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). (concepto + ellos)
# Calcular la suma de los números positivos y el producto de los negativos.
# Calcular la suma de los números ingresados y el promedio de los mismos.

contador = 0
salida = "si"
acumulador_total = 0
acumulador_suma = 0
acumulador_producto = 1

while salida == "si":
    numero_ingresado = int(input("Ingrese un numero: "))
    acumulador_total += numero_ingresado
    if numero_ingresado >= 0:
        acumulador_suma += numero_ingresado
    else:
        acumulador_producto = acumulador_producto * numero_ingresado
    
    contador += 1
    salida = input("¿Desea continuar? si / no: ")

promedio = acumulador_total/contador  

print(f"La suma de los numero positivos es: {acumulador_suma} \nEl producto de los numeros negativos es: {acumulador_producto}")