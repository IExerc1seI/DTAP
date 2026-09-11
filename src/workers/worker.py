from src.domain.entities.test import Test
from src.workers.executor import TestExecutor
from src.infrastructure.logging import logger

class Worker:
    def __init__(self):
        self.executor = TestExecutor()

    async def run(self, test: Test):
        logger.info(f"Worker started executing test: {test.name}")
        return await self.executor.execute(test)