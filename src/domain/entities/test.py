from dataclasses import dataclass
import datetime
from test_step import TestStep

@dataclass
class Test:
    id: int
    name: str
    description: str
    steps: list(TestStep)
    created_at: datetime
    updated_at: datetime