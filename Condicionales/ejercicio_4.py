# A partir del ingreso de la altura de un basquetbolista determinar si es pivot o no. Para serlo el mismo deberá medir más de 1.80 metros.

altura_ingresada = input("Ingrese sue altura: ")
altura_ingresada = float(altura_ingresada)

if altura_ingresada > 179:
    print("Sos pivot.")
else:
    print("No sos pivot.")