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


lado_bc = input("Ingrese las medida BC en cm: ")
lado_cd = input("Ingrese las medida CD en cm: ")
lado_da = input("Ingrese las medida DA en cm: ")

lado_bc = int(lado_bc)
lado_cd = int(lado_cd)
lado_da = int(lado_da)

# Agregamos un nuevo punto llamado E, el cual sera la intercepcion de la diagonal mayor con la diagonal menor
lado_ce = lado_cd / 2

lado_ae = (lado_da**2 - lado_ce**2)**0.5

print ((5**2 - 4**2)**0.5)


#print(f"El total de varillas es de {varillas} cm")