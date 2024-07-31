'''1- Debemos realizar la carga de 5(cinco) productos de prevención de contagio, (3 veces)
de cada una debo obtener los siguientes datos:
el tipo (validar "barbijo" , "jabón" o "alcohol", “guardapolvo”, “guantes”) ,
el precio (validar entre 100 y 300),
la cantidad de unidades (no puede ser 0 o negativo y no debe superar las 1000 unidades),
la Marca y el fabricante.

Se debe Informar al usuario lo siguiente:
a) Del más caro de los Barbijos, la cantidad de unidades y el fabricante
b) Del ítem con más unidades, el fabricante
c) Cuántas unidades de jabones hay en total'''

contador = 0
acumulador_jabones = 0

while contador < 15:
    tipo_producto = input("Ingrese el tipo de producto (barbijo / jabon / alcohol / guardapolvo / guantes): ")
    while tipo_producto != "barbijo" and tipo_producto != "jabon" and tipo_producto != "alcohol" and tipo_producto != "guardapolvo" and tipo_producto != "guantes":
        tipo_producto = input("¡Producto invalido! \nIngrese el tipo de producto: ")
    precio_producto = float(input("Ingrese su precio (minimo 100 / maximo 300): "))
    while precio_producto < 100 or precio_producto > 300:
        precio_producto = float(input("¡Precio invalido!\nIngrese su precio: "))    
    unidades_producto = int(input("Ingrese la cantidad (minimo 1 / maximo 1000): "))
    while unidades_producto < 1 or unidades_producto > 1000:
        unidades_producto = int(input("¡Cantidad invalida!\nIngrese la cantidad: "))
    marca_producto = input("Ingrese la marca: ")
    fabricante_producto = input("Ingrese el fabricante: ")

    if contador == 0:
        precio_barbijo_mas_caro = precio_producto
        cantidad_barbijo_mas_caro = unidades_producto
        fabricante_barbijo_mas_caro = fabricante_producto
        item_mas_unidades = unidades_producto
    if tipo_producto == "barbijo" and precio_producto > precio_barbijo_mas_caro:
        precio_barbijo_mas_caro = precio_producto
        cantidad_barbijo_mas_caro = unidades_producto
        fabricante_barbijo_mas_caro = fabricante_producto
    if unidades_producto > item_mas_unidades:
        fabricante_item_mas_unidades = fabricante_producto
    if tipo_producto == "jabon":
        acumulador_jabones += unidades_producto

    contador += 1

mensaje_final = f'''
---------------------------
RESULTADOS:
A- Barbijo mas caro: {fabricante_barbijo_mas_caro} - {cantidad_barbijo_mas_caro} unidades.
B- Fabricante del item con mas unidades: {fabricante_item_mas_unidades}
C- Total de jabones: {acumulador_jabones} unidades.

'''

print(mensaje_final)