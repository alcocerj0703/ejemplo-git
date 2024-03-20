import suma
import resta
import multiplicacion
import division

def validar_numero(prompt):
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
            print("Error: Por favor ingresa un número válido.")

def menu():
    print("Calculadora Simple")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

while True:
    menu()
    opcion = input("Selecciona una opción: ")

    if opcion == '5':
        print("¡Hasta luego!")
        break
    elif opcion in {'1', '2', '3', '4'}:
        num1 = validar_numero("Ingrese el primer número: ")
        num2 = validar_numero("Ingrese el segundo número: ")

        if opcion == '1':
            print("Resultado:", suma.sumar(num1, num2))
        elif opcion == '2':
            print("Resultado:", resta.restar(num1, num2))
        elif opcion == '3':
            print("Resultado:", multiplicacion.multiplicar(num1, num2))
        elif opcion == '4':
            print("Resultado:", division.dividir(num1, num2))
    else:
        print("Opción no válida. Por favor selecciona una opción del menú.")

