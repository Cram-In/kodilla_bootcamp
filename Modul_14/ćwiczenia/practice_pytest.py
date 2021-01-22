import pytest


def divide(x, y):
    return x / y


def test_divide():
    result = divide(54, 6)
    assert result == 9


def test_divide_exception():
    with pytest.raises(Exception):
        x = 1 / 0


def test_divide_exception():
    with pytest.raises(Exception) as e_info:
        x = 1 / 0


def test_divide_fails():
    with pytest.raises(Exception) as e_info:
        x = 1 / 1
