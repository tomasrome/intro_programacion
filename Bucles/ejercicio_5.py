# Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio. Mostrar por pantalla.

# Tomás Romero
# Bucles 5

contador = 0
acumulador = 0

while contador < 5:
    contador +=1
    numero_ingresado = int(input("Ingrese un numero: "))
    acumulador += numero_ingresado

promedio = acumulador/contador  

print(f"La suma de los numeros es {acumulador} y el promedio es {promedio}")