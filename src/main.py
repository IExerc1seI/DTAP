import asyncio
from pathlib import Path

from src.application.parsers.yaml_parser import YamlParser
from src.workers.worker_pool import WorkerPool


async def main():
    parser = YamlParser()

    tests = [
        parser.load(Path("docs/examples/sample-test.yaml")),
        parser.load(Path("docs/examples/device-health-check.yaml")),
        parser.load(Path("docs/examples/stress-test.yaml")),
    ]

    pool = WorkerPool(
        num_workers=3
    )

    results = await pool.run_tests(
        tests
    )

    print(
        f"Results: {results}"
    )


if __name__ == "__main__":
    asyncio.run(main())