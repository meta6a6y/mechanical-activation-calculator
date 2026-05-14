import numpy as np


def calculate_deviations(values, time):
    """
    Расчет отклонений от предыдущего значения - мгновенная скорость
    value_0: начальное значение (при t=0)
    delta_t: разница во времени
    """
    deviations = []

    for i in range(1, len(values)):
        delta_t = time[i] - time[i - 1]
        deviation = (values[i] - values[i-1]) / delta_t
        deviations.append(deviation)

    return np.array(deviations)