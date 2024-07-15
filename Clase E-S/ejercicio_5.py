#Realizar un programa que permita el ingreso de dos números. Calcular la suma, resta, multiplicación y división de los mismos. 
# Mostrar los resultados por pantalla. Utilizar una variable para mostrar el resultado (concatenar).

# Tomas Romero
# E/S 5

primer_numero_ingresado = input("Ingrese el primer numero: ")
segundo_numero_ingresado = input("Ingrese el segundo numero: ")

primer_numero_ingresado = float(primer_numero_ingresado)
segundo_numero_ingresado = float(segundo_numero_ingresado)

suma = primer_numero_ingresado + segundo_numero_ingresado
resta = primer_numero_ingresado - segundo_numero_ingresado
multiplicacion = primer_numero_ingresado * segundo_numero_ingresado
division = primer_numero_ingresado / segundo_numero_ingresado

print(f"La suma de los numeros es: {suma}")
print(f"La resta de los numeros es: {resta}")
print(f"La multiplicacion de los numeros es: {multiplicacion}")
print(f"La division de los numeros es: {division}")