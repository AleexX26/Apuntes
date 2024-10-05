precios_cafe = [("cafe A", 2.50), ("cafe B", 3.00), ("cafe C", 3.50)]

# for cafe, precio in precios_cafe:
#     print(precio)

def cafeMasCaro(lista_precios):
    
    precio_mas_caro = 0
    nombre_cafe_mas_caro = ""
    
    for cafe, precio in lista_precios:
        if precio > precio_mas_caro:
            precio_mas_caro = precio
            nombre_cafe_mas_caro = cafe
        else:
            pass
    
    return(nombre_cafe_mas_caro, precio_mas_caro)

print(cafeMasCaro(precios_cafe))