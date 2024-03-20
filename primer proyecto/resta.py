def resta(num1, num2):
  """
  Realiza la resta de dos números.

  Args:
    num1 (float): Primer número.
    num2 (float): Segundo número.

  Returns:
    float: Resultado de la resta.
  """
  return num1 - num2

def main():
  """
  Función principal que ejecuta la calculadora.
  """
  while True:
    # Mostrar menú
    print("**Calculadora simple**")
    print("1. Resta")
    print("2. Salir")

    # Obtener la opción del usuario
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
      # Obtener los números del usuario
      num1 = float(input("Ingrese el primer número: "))
      num2 = float(input("Ingrese el segundo número: "))

      # Validar los números
      if not isinstance(num1, float) or not isinstance(num2, float):
        print("Error: Los valores ingresados no son números válidos.")
        continue

      # Realizar la resta
      resultado = resta(num1, num2)

      # Mostrar el resultado
      print(f"{num1} - {num2} = {resultado}")

    elif opcion == 2:
      # Salir de la calculadora
      print("¡Hasta luego!")
      break

    else:
      # Opción no válida
      print("Error: Opción no válida.")

if __name__ == "__main__":
  main()
