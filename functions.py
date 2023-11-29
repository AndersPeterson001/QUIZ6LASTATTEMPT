# app/functions.py

def add_numbers(a, b):
    """
    Add two numbers.

    Parameters:
    a (float): The first number to be added.
    b (float): The second number to be added.

    Returns:
    float: The sum of a and b.
    """
    return a + b

def subtract_numbers(a, b):
    """
    Subtract one number from another.

    Parameters:
    a (float): The number from which b will be subtracted.
    b (float): The number to subtract from a.

    Returns:
    float: The result of a minus b.
    """
    return a - b

def divide_numbers(a, b):
    """
    Divide one number by another.

    Parameters:
    a (float): The numerator.
    b (float): The denominator. Must not be zero.

    Returns:
    float: The result of a divided by b.

    Raises:
    ValueError: If b is zero, as division by zero is not allowed.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def multiply_numbers(a, b):
    """
    Multiply two numbers.

    Parameters:
    a (float): The first number to be multiplied.
    b (float): The second number to be multiplied.

    Returns:
    float: The product of a and b.
    """
    return a * b
