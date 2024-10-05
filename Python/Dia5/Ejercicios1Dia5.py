def devolver_distintos(num1, num2, num3):
    total = (num1+num2+num3)
    
    if total > 15:
        print(f"El resultado es {total}, que es mayor que 15.")
        return total
    elif total < 10:
        print(f"El resultado es {total}, que es menor que 10.")
        return total
    else:
        print(f"El resultado es {total}, que está entre 10 y 15.")
        return total

numeros = (5,8,3)

print(devolver_distintos(*numeros))