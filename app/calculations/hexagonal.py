import math


def calculate_a_hexagonal(d_hk0, h, k):
    """
    Расчет параметра решетки a для гексагональной сингонии
    Для плоскости hk0 (l = 0)
    """
    a = 2 * d_hk0 * math.sqrt((h ** 2 + h * k + k ** 2) / 3)
    return a


def calculate_c_hexagonal(d_hkl, h, k, l, a):
    """
    Расчет параметра решетки c для гексагональной сингонии
    Для плоскости с l ≠ 0
    """
    term = (4 / 3) * (h ** 2 + h * k + k ** 2) / (a ** 2)
    c = l / math.sqrt((1 / d_hkl ** 2) - term)
    return c