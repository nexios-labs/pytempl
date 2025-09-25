from dataclasses import dataclass
from typing import List


@dataclass
class ComponentDirective:
    name: str
    value: List[str]
