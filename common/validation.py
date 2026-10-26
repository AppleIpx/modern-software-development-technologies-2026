def is_strict_int(value):
    """Целое число, но не bool: True проходит isinstance(value, int), хотя числом считаться не должно."""
    return type(value) is int


def is_strict_bool(value):
    return type(value) is bool


def is_positive_int(value):
    return is_strict_int(value) and value > 0
