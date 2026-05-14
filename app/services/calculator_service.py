import numpy as np

from app.calculations.cubic import calculate_a_cubic
from app.calculations.hexagonal import calculate_a_hexagonal, calculate_c_hexagonal
from app.calculations.deviations import calculate_deviations
from app.models.result import CalculationResult


def calculate_sample(sample):
    try:
        if sample.crystal_system == "cubic":
            a_values = np.array([
                calculate_a_cubic(d, sample.h, sample.k, sample.l)
                for d in sample.d_values
            ])

            deviations = calculate_deviations(a_values, sample.time_values)

            return CalculationResult(
                sample_name=sample.name,
                parameter_type=f"a (cubic) [{sample.h}{sample.k}{sample.l}]",
                lattice_parameters=a_values.tolist(),
                time_values=sample.time_values,
                deviations=deviations.tolist()
            )

        elif sample.crystal_system == "hexagonal":
            if sample.l == 0:
                a_values = np.array([
                    calculate_a_hexagonal(d, sample.h, sample.k)
                    for d in sample.d_values
                ])

                deviations = calculate_deviations(a_values, sample.time_values)

                return CalculationResult(
                    sample_name=sample.name,
                    parameter_type=f"a (hexagonal) [{sample.h}{sample.k}0]",
                    lattice_parameters=a_values.tolist(),
                    time_values=sample.time_values,
                    deviations=deviations.tolist()
                )

            elif sample.h == 0 and sample.k == 0 and sample.l != 0:
                c_values = np.array([
                    d * abs(sample.l)
                    for d in sample.d_values
                ])

                deviations = calculate_deviations(c_values, sample.time_values)

                return CalculationResult(
                    sample_name=sample.name,
                    parameter_type=f"c (hexagonal) [00{sample.l}]",
                    lattice_parameters=c_values.tolist(),
                    time_values=sample.time_values,
                    deviations=deviations.tolist()
                )

            else:
                if sample.a_parameter is None:
                    raise ValueError(
                        f"Для расчета c необходимо знать параметр a. "
                        f"Укажите a_parameter для образца {sample.name}"
                    )

                c_values = np.array([
                    calculate_c_hexagonal(d, sample.h, sample.k, sample.l, sample.a_parameter)
                    for d in sample.d_values
                ])

                deviations = calculate_deviations(c_values, sample.time_values)

                return CalculationResult(
                    sample_name=sample.name,
                    parameter_type=f"c (hexagonal) [{sample.h}{sample.k}{sample.l}]",
                    lattice_parameters=c_values.tolist(),
                    time_values=sample.time_values,
                    deviations=deviations.tolist()
                )

        else:
            raise ValueError(f"Неизвестная сингония: {sample.crystal_system}")

    except Exception as e:
        return CalculationResult(
            sample_name=sample.name,
            parameter_type="error",
            lattice_parameters=[],
            deviations=[],
            error=str(e)
        )


def calculate_samples(samples):
    results = []
    for sample in samples:
        result = calculate_sample(sample)
        results.append(result)
    return results
