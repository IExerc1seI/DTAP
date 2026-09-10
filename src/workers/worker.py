from src.domain.entities.test import Test
from src.workers.executor import TestExecutor

class Worker:
    def __init__(self):
        self.executor = TestExecutor()

    async def run(self, test: Test):
        return await self.executor.execute(test)