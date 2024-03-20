def validar_numero_entero_positivo(numero):
    try:
        numero_entero = int(numero)
        if numero_entero <= 0:
            return False, "El número debe ser positivo."
        else:
            return True, "Número válido."
    except ValueError:
        return False, "El valor ingresado no es un número entero."
