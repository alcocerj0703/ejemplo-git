import validador

def dividir(a, b):
    validacion, mensaje = validador.validar(a, b)
    if validacion:
        if b != 0:
            return a / b
        else:
            return "Error: No se puede dividir entre cero"
    else:
        return "Error: " + mensaje

