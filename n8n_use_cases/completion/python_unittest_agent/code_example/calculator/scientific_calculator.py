import math
from base_calculator import BaseCalculator


class ScientificCalculator(BaseCalculator):
    def power(self, base, exponent):
        return math.pow(base, exponent)

    def square_root(self, x):
        if x < 0:
            raise ValueError("Cannot take square root of a negative number.")
        return math.sqrt(x)

    def logarithm(self, x, base=10):
        if x <= 0:
            raise ValueError("Logarithm undefined for non-positive values.")
        return math.log(x, base)
