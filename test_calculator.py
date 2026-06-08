import pytest
from calculator import add, subtract, multiply, divide, is_even


def test_add_positive():
    assert add(5, 3) == 8


def test_add_negative():
    assert add(-5, 3) == -2


def test_add_floats():
    assert add(2.5, 3.5) == 6.0


def test_add_raises_error():
    with pytest.raises(ValueError):
        add("5", 3)


def test_subtract():
    assert subtract(10, 4) == 6


def test_multiply():
    assert multiply(6, 7) == 42


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)


def test_is_even():
    assert is_even(4) is True
    assert is_even(7) is False


def test_is_even_raises():
    with pytest.raises(ValueError):
        is_even(4.5)
        