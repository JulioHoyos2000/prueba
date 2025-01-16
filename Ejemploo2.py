def calcular(producto, suma):
    a, b = producto
    return a * b + suma

def mostrar_resultado(resultado):
    print("El resultado es:", resultado)

def principal():
    valores_producto = (5, 3)
    valor_suma = 7
    resultado = calcular(valores_producto, valor_suma)
    mostrar_resultado(resultado)

principal()
