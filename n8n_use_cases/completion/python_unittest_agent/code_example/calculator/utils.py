def is_even(n):
    return n % 2 == 0


def is_odd(n):
    return n % 2 != 0


def clamp(value, min_value, max_value):
    if min_value > max_value:
        raise ValueError("min_value cannot be greater than max_value.")
    return max(min_value, min(value, max_value))
