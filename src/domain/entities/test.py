from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4
from src.domain.entities.test_step import TestStep

@dataclass
class Test:
    id: UUID = field(default_factory=uuid4)
    name: str = ""
    description: str = ""
    steps: list[TestStep] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)

    def add_step(self, step: TestStep):
        self.steps.append(step)
        self.updated_at = datetime.utcnow()

    def remove_step(self, step_id:UUID):
        self.steps =[
            step
            for step in self.steps
            if step.id != step_id
        ]
        self.updated_at = datetime.utcnow()

    def update_description(self, description:str):
        self.description = description
        self.updated_at = datetime.utcnow()