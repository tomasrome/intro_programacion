#4- Realizar un programa que permita el ingreso de dos números. Realizar la suma de los mismos y mostrar el resultado por pantalla 
# con el siguiente formato: “La suma de los dos números es: ___”

# Tomás Romero
# E/S 4

primer_numero_ingresado = input("Ingrese su primer numero: ")
segundo_numero_ingresado = input("Ingrese su segundo numero: ")

primer_numero_ingresado = int(primer_numero_ingresado)
segundo_numero_ingresado = int(segundo_numero_ingresado)

suma_numeros_ingresados = primer_numero_ingresado + segundo_numero_ingresado

print(f"La suma de los numeros es: {suma_numeros_ingresados}.")


