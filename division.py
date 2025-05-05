def dividir(a, b):

    if b == 0:
        return "Error: no se puede dividir por cero"
    
    return a / b

num1 = float(input("Ingrese el dividendo: "))
num2 = float(input("Ingrese el divisor: "))

resultado = dividir(num1, num2)
print("Resultado:", resultado)