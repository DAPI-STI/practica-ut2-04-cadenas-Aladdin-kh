"""
Ejercicio 2: leer un nombre completo (nombre + apellidos) y mostrar:

Todo en minúsculas.

Todo en mayúsculas.

Capitalizado (primera letra de cada palabra en mayúscula).

La función devolverá una tupla: (minusculas, mayusculas, capitalizado).
"""

def name_variants(full_name: str) -> tuple[str, str, str]:
    """Devuelve (minusculas, MAYUSCULAS, Capitalizado-Por-Palabra)."""
    return (full_name.lower(), full_name.upper(), full_name.title())
    # TODO: usa los métodos .lower(), .upper() y .title() de str
    raise NotImplementedError("Implementa name_variants(full_name)")  