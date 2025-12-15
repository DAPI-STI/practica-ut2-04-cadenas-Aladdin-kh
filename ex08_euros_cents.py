"""
Ejercicio 8: leer un precio con dos decimales y mostrar euros y céntimos por separado.

La función:

Recibe una cadena como "123.45" o "123,45".

Devuelve una tupla (euros, centimos) como enteros.

Valida que haya exactamente dos decimales; en caso contrario, ValueError.
"""

def euros_cents(price_str: str) -> tuple[int, int]:
    """Separa la parte entera (euros) y los céntimos a partir de una cadena."""
    # TODO: sustituye coma por punto, separa, valida y convierte a enteros
    price_str = price_str.replace(",", ".")
    partes = price_str.split(".")
    if len(partes) != 2 or len(partes[1]) != 2 or not partes[0].isdigit() or not partes[1].isdigit():
        raise ValueError("El formato del precio es incorrecto.")
    euros = int(partes[0])
    centimos = int(partes[1])
    return (euros, centimos)
    raise NotImplementedError("Implementa euros_cents(price_str)")