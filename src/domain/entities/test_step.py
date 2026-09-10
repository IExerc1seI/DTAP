from dataclasses import dataclass, field
from uuid import UUID, uuid4

@dataclass
class TestStep:
    id: UUID = field(default_factory=uuid4)
    action: str = ""
    parameters: dict = field(default_factory=dict)
    order: int = 0