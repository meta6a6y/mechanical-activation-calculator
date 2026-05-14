import math


def calculate_a_cubic(d_hkl, h, k, l):
    """
    Расчет параметра решетки a для кубической сингонии
    d_hkl: межплоскостное расстояние
    h, k, l: индексы Миллера
    """
    a = d_hkl * math.sqrt(h**2 + k**2 + l**2)
    return a