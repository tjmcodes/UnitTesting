import pytest
from triangle_func import triangle_type


def test_triangle_equilateral():
    assert triangle_type(1, 1, 1) == "Equilateral"
    assert triangle_type(1, 1, 1) == "Equilateral"
    assert triangle_type(1, 1, 1) == "Equilateral"


def test_triangle_isosceles():
    assert triangle_type(23, 23, 25) == "Isosceles"
    assert triangle_type(12, 12, 12.3) == "Isosceles"


def test_triangle_scalene():
    assert triangle_type(23, 34, 25) == "Scalene"
    assert triangle_type(12, 12.3, 11.3) == "Scalene"


def test_triangle_validate_negative():
    assert triangle_type(-23, -24, -23) == "Error"
    assert triangle_type(-24, 24, 24) == "Error"


def test_triangle_validate_integers():
    assert triangle_type("24", "24", "24") == "Invalid. Only accepts integer"
    assert triangle_type("24.2", "24.5", "24.67") == "Invalid. Only accepts integer"


def test_triangle_validate():
    assert triangle_type(10, 2, 1) == "Not a triangle"
    assert triangle_type(True, 14, 24) == "Not a triangle"
