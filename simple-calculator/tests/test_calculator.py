from calculator.calculator import add


def test_add():
    # Given
    a = 3
    b = 5
    # When
    result = add(a, b)
    # Then
    assert result == 8


def test_add_short():
    assert add(3, 5) == 8
