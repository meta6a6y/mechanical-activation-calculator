from dataclasses import dataclass
from typing import List, Optional


@dataclass
class CalculationResult:
    """
    Результат расчета параметров кристаллической решетки
    """
    sample_name: str
    parameter_type: str
    lattice_parameters: List[float]
    deviations: List[float]
    error: Optional[str] = None
    time_values: Optional[List[float]] = None

