#Al ejecutar el programa, se deberá calcular una nota aleatoria entre el 1 y el 10 inclusive, para luego mostrar un mensaje según el valor:
#6, 7, 8, 9 y 10 ---> Promoción directa, la nota es ...
#4 y 5           ---> Aprobado, la nota es ...
#1, 2 y 3        ---> Desaprobado, la nota es ...

import random

numero_aleatorio = random.randint(1,10)

if numero_aleatorio > 5:
    print(f"Promoción directa, la nota es {numero_aleatorio}")
elif numero_aleatorio < 4:
    print(f"Desaprobado, la nota es {numero_aleatorio}")
else:
    print(f"Aprobado, la nota es {numero_aleatorio}")