import math

class Calculator:
    def __init__(self) -> None:
        self.__result: float = 0.0

    def add(self, a: float) -> 'Calculator':
        self.__result += a
        return self

    def subtract(self, a: float) -> 'Calculator':
        self.__result -= a
        return self

    def multiply(self, a: float) -> 'Calculator':
        self.__result *= a
        return self

    def divide(self, a: float) -> 'Calculator':
        if a == 0:
            raise ValueError("Cannot divide by zero")
        self.__result /= a
        return self

    def modulo(self, a: float) -> 'Calculator':
        if a == 0:
            raise ValueError("Cannot divide by zero")
        self.__result %= a
        return self

    def power(self, a: float) -> 'Calculator':
        self.__result **= a
        return self

    def square_root(self) -> 'Calculator':
        if self.__result < 0:
            raise ValueError("Cannot take the square root of a negative number")
        self.__result = math.sqrt(self.__result)
        return self

    def clear(self) -> 'Calculator':
        self.__result = 0.0
        return self

    def set_result(self, value: float) -> 'Calculator':
        self.__result = value
        return self

    def get_result(self) -> float:
        return self.__result
