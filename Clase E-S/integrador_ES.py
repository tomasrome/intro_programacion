# Integrador E/S

# La juguetería El MUNDO DE CHARLY nos encarga un programa para conocer qué cantidad de materiales se necesita para la fabricación de distintos juguetes.

# CONFECCIÓN DE UN COMETA: 

# Medidas:
# AB = Diágonal mayor
# DC = Diágonal menor
# BD y BC = lados menores
# AD y AC = lados mayores


# El usuario ingresará las medidas  BC, CD y DA.

# Detalles de construcción

# Debemos tener en cuenta que la estructura del cometa estará dada por un perímetro de varillas de plástico y los correspondientes 
# entrecruces (DC y AB) del mismo material para mantener la forma del cometa.
# El cometa estará construido con papel de alta resistencia. La cola del mismo se construirá con el mismo papel que el cuerpo y 
# representará un 10% adicional del necesario para el cuerpo.
# Necesitamos saber cuántos Mts de varillas de plástico y cuántos de papel son necesarios para la construcción en masa de 10 cometas. 
# Tener en cuenta que los valores de entrada están expresados en Cms.

# Tomás Romero
# Integrador E/S

import math

lado_bc = input("Ingrese las medida BC en cm: ")
lado_cd = input("Ingrese las medida CD en cm: ") 
lado_da = input("Ingrese las medida DA en cm: ")

lado_bc = float(lado_bc)
lado_da = float(lado_da) 
diagonal_menor = float(lado_cd)

diagonal_mayor_uno = math.sqrt(lado_da**2 - (diagonal_menor / 2)**2)
diagonal_mayor_dos = math.sqrt(lado_bc**2 - (diagonal_menor / 2)**2)
diagonal_mayor = diagonal_mayor_uno + diagonal_mayor_dos

varillas_total_cm = diagonal_menor + diagonal_mayor + 2*(lado_bc + lado_da)
perimetro = 2*(lado_bc + lado_da)
varillas_total_metros = varillas_total_cm / 100

area_cometa_cm2 =  (diagonal_menor * diagonal_mayor) / 2
area_cometa_m2 = area_cometa_cm2 / 10000
papel_total_m2 = area_cometa_m2 * 1.1


varillas_diez_cometas = varillas_total_metros * 10
papel_diez_cometas = papel_total_m2 * 10

print (f"Para la producción de 10 cometas se necesitan {varillas_diez_cometas}m de varillas y {papel_diez_cometas}m2 de papel de alta resistencia.")
