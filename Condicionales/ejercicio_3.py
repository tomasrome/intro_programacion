#A partir del ingreso de una edad, determinar si la persona es mayor de edad o no. Si es mayor de 18 se mostrará el mensaje “UD ES MAYOR DE EDAD” caso contrario “UD ES MENOR DE EDAD”.

# Tomás Romero
# E/S 8

edad_ingresada = input("Ingrese sue edad: ")
edad_ingresada = int(edad_ingresada)

if edad_ingresada > 17:
    print("UD ES MAYOR DE EDAD")
else:
    print("UD ES MENOR DE EDAD")

