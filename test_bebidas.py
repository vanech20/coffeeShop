import pytest
from bebidas import validate_bebida

@pytest.mark.parametrize("array, expected", [
    ("C, 1, 2, 3, 4, 5", False), # Nombre con menos de 2 caracteres
    ("Teeeeeeeeeeeeeeeeeeeeeeeee, 2, 3, 4, 5, 6", False), # Nombre con mas de 15 caracteres
    ("Ch0c0l4t3, 7, 8, 9, 10, 11", False), # Nombre con caracteres no alfabéticos
    ("Cafeee, 1, 2, 3, 4, 5", True), # Nombre dentro del rango
    ("Te, 1, 2, 3, 4, 5, 6", False), # Bebida con más de 6 tamaños
    ("Cafe, 48", True), # Bebida con al menos un tamaño
    ("Cafeee, 1 , 2, 3", True),  # Número de tamaños dentro del rango
    ("Chocolate, 1, 5, 12, 22, 49", False), # Tamaño mayor a 48
    ("Te, 0, 11, 13, 15, 17", False), # Tamaño menor a 1
    ("Cafe, 1, 45, 46, 47, 48", True), # Tamaños dentro del límite
    ("Chocolate, 1, 2, 3, 5, 4", False), # Los tamaños no son ascendentes
    ("Te, 7, 8, 9, 10, 11", True), # Los tamaños son ascendentes
    ("Cafe, 7, 8, 9, 9, 10", False), # Tamaño repetido (no ascendente)
    ("Chocolate, 6, -8, 9, 10, 12", False), # El tamaño no es un número entero
    ("5, Cafe, 7, 8, 9", False), # El nombre no es el primer parámeto
    ("Te, 1, 2", True), # Nombre en en la primera posición
    ("Cafe,, 1, 2, 3, 4, 5", False), # La entrada este separada por más de una coma
    ("   Chocolate ,12,   13 ,    14  ,    15", True), # La entrada contiene espacios en blanco
])
def test_validate_bebida(array, expected):
    assert validate_bebida(array) == expected