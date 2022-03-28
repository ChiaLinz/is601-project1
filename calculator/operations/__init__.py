""" These are the Operation Classes"""


class Addition:
    """ This is the addition class"""

    # this defines a static method that you can use without instantiating the calculator class
    # If you can go to the store and buy it, it is an object.  If you can't buy it then its a static method
    @staticmethod
    def add(value_1, value_2):
        return value_1 + value_2


class Subtraction:

    @staticmethod
    def subtract(value_1, value_2):
        return value_1 - value_2


class Multiplication:

    @staticmethod
    def multiply(value_1, value_2):
        return value_1 * value_2


class Division:

    @staticmethod
    def divide(value_1, value_2):
        return value_1 / value_2