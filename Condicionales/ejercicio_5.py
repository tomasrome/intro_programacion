#Obtener la edad,  transformarlo en número y calcular si es mayor, niño/a(menor de 10) o pre-adolescente. (edad entre 10 y 13 años) o adolescente (edad entre 13 y 17 años) de edad, 

edad_ingresada = input("Ingrese sue edad: ")
edad_ingresada = int(edad_ingresada)

if edad_ingresada >= 18:
    print("Sos mayor de edad.")
elif edad_ingresada <= 10:
    print("Sos niño/a")
elif edad_ingresada <= 13:
    print("Sos pre-adolescente")
else:
    print("Sos adolescente")