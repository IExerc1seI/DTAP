import asyncio
from src.domain.entities.test import Test
from src.workers.worker import Worker

class WorkerPool:
    def __init__(self, num_workers: int):
        self.num_workers = num_workers
        self.workers = [Worker() for _ in range(num_workers)]

    async def run_tests(self, tests: list[Test]):
        tasks = []
        for i, test in enumerate(tests):
            worker = self.workers[i % self.num_workers]
            tasks.append(worker.run(test))
        return await asyncio.gather(*tasks)