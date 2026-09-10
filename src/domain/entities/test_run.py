from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4
from src.domain.enums.run_status import RunStatus

@dataclass
class TestRun:
    id: UUID = field(default_factory=uuid4)
    test_id: UUID = field(default_factory=uuid4)
    status: RunStatus
    started_at: datetime = field(default=datetime.utcnow)
    finished_at: datetime = field(default=datetime.utcnow)

    def start(self):
        self.status = RunStatus.RUNNING
        self.started_at = datetime.utcnow()

    def failed(self):
        self.status = RunStatus.FAILED
        self.finished_at = datetime.utcnow()

    def finish(self):
        self.status = RunStatus.PASSED
        self.finished_at = datetime.utcnow()

    def cancel(self):
        self.status = RunStatus.CANCELLED
        self.finished_at = datetime.utcnow()
