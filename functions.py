def add(a, b):
    """Addition function.

    Args:
        a (int): The first number to be added.
        b (int): The second number to be added.

    Returns:
        int: The sum of `a` and `b`.
    """
    return a + b


def subtract(a, b):
    """Subtraction function.

    Args:
        a (int): The number to subtract from.
        b (int): The number to subtract.

    Returns:
        int: The result of subtracting `b` from `a`.
    """
    return a - b


def multiply(a, b):
    """Multiplication function.

    Args:
        a (int): The first number to be multiplied.
        b (int): The second number to be multiplied.

    Returns:
        int: The product of `a` and `b`.
    """
    return a * b


def divide(a, b):
    """Division function.

    Args:
        a (int): The number to divide.
        b (int): The number to divide by.

    Raises:
        ValueError: If `b` is zero.

    Returns:
        float: The result of dividing `a` by `b`.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b


# Unit Tests
def test_add():
    """Unit tests for the `add` function."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_subtract():
    """Unit tests for the `subtract` function."""
    assert subtract(2, 3) == -1
    assert subtract(-1, 1) == -2
    assert subtract(0, 0) == 0


def test_multiply():
    """Unit tests for the `multiply` function."""
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(0, 0) == 0


def test_divide():
    """Unit tests for the `divide` function."""
    assert divide(6, 3) == 2
    assert divide(-1, 1) == -1
    assert divide(0, 5) == 0
    try:
        divide(6, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero!"
