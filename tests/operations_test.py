"""Testing the calculator operations """

from calculator.operations import Addition, Subtraction, Multiplication, Division


def test_calculator_operations_add():
    """Testing the Calculator"""
    assert Addition.add(2, 3) == 5


def test_calculator_operations_subtract():
    """Testing the Calculator"""
    assert Subtraction.subtract(7, 3) == 4


def test_calculator_operations_multiply():
    """Testing the Calculator"""
    assert Multiplication.multiply(6, 6) == 36

def test_calculator_operations_divide():
    """Testing the Calculator"""
    assert Division.divide(6, 6) == 1
