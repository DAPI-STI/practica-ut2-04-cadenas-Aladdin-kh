"""
Ejercicio 9: leer una fecha (día, mes, año) introducida como "dd/mm/aaaa"
y mostrar cada componente por separado.

La función:

Recibe un string con formato "d/m/aaaa" o "dd/mm/aaaa".

Devuelve (dia, mes, año) como enteros.

Si el formato o los rangos son incorrectos, lanza ValueError.
"""

def parse_date(date_str: str) -> tuple[int, int, int]:
    """Devuelve (día, mes, año) como enteros a partir de una cadena d/m/aaaa."""
    partes = date_str.split("/")
    if len(partes) != 3:
        raise ValueError("El formato de la fecha es incorrecto.")
    dia_str, mes_str, anio_str = partes
    if not (dia_str.isdigit() and mes_str.isdigit() and anio_str
              .isdigit()):
          raise ValueError("La fecha debe contener solo números.")
    dia = int(dia_str)
    mes = int(mes_str)
    anio = int(anio_str)
    if not (1 <= dia <= 31):
        raise ValueError("El día debe estar entre 1 y 31.")
    if not (1 <= mes <= 12):
        raise ValueError("El mes debe estar entre 1 y 12.")
    if anio < 0:
        raise ValueError("El año no puede ser negativo.")
    return (dia, mes, anio)
    # TODO: usa split("/"), convierte a int y valida rangos sencillos
    raise NotImplementedError("Implementa parse_date(date_str)")