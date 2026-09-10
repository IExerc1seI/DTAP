from dataclasses import dataclass, field
from uuid import UUID, uuid4
from datetime import datetime

@dataclass
class TestResult:
    id: UUID = field(default_factory=uuid4)
    run_id: UUID = field(default_factory=uuid4)
    success: bool = False
    duration: float = 0.0
    logs: list[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.utcnow)

    def add_log(self, message: str):
        self.logs.append(message)