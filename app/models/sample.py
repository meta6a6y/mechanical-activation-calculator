from dataclasses import dataclass
from typing import List, Optional



@dataclass
class Sample:
    name: str
    crystal_system: str
    h: int
    k: int
    l: int
    d_values: List[float]
    time_values: List[float]
    a_parameter: Optional[float] = None
