# Solicitar un número al usuario
numero = float(input("Ingrese un número para calcular su raíz cuadrada: "))

# Verificar si el número es válido
if numero >= 0:
    raiz_cuadrada = numero ** 0.5
    print(f"La raíz cuadrada de {numero} es {raiz_cuadrada}")
else:
    print("No se puede calcular la raíz cuadrada de un número negativo.")