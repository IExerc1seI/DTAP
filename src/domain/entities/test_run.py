from dataclasses import dataclass
import datetime

@dataclass
class TestRun:
    id: int
    test_id: int
    status: RunStatus
    started_at: datetime | None
    finished_at: datetime  | None
