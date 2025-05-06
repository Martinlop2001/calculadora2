from suma import suma
from resta import resta
from multiplicacion import multiplicacion
from division import division

print("Seleccione entre (1 - 2 - 3 - 4)")

print("1 - Suma")
print("2 - Resta")
print("3 - Division")
print("4 - Multiplicación")

opc = int(input(": "))

if opc == 1:
    
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese un numero: "))
    suma = suma(num1, num2)
    print ("El resultado de la suma es: ", suma)

elif opc == 2:

    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese un numero: "))
    resta = resta(num1, num2)
    print ("El resultado de la resta es: ", resta)

elif opc == 3:

    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese un numero: "))
    division = division(num1, num2)
    print ("El resultado de la division es: ", division)

elif opc == 4:

    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese un numero: "))
    multiplicacion = multiplicacion(num1, num2)
    print ("El resultado de la multiplicacion es: ", multiplicacion)