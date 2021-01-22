def add(x, y):
    return x + y


def test_add():
    result = add(2, 2)
    assert result == 4


def test_add_negative():
    result = add(-1, -1)
    assert result == -2
