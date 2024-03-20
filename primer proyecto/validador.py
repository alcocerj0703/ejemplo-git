def validar(numero1, numero2):
    try:
        numero_entero1 = int(numero1)
        numero_entero2 = int(numero2)
        if numero_entero1 <= 0 or numero_entero2 <= 0:
            return False, "Ambos números deben ser positivos."
        else:
            return True, "Números válidos."
    except ValueError:
        return False, "Los valores ingresados no son números enteros."