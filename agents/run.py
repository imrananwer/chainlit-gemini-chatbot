from dataclasses import dataclass
from typing import Any

@dataclass
class RunConfig:
    model: Any
    model_provider: Any
    tracing_disabled: bool = True
