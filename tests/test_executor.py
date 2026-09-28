import pytest
from pathlib import Path

from src.application.parsers.yaml_parser import YamlParser
from src.workers.executor import TestExecutor

@pytest.mark.asyncio
async def test_executor_run():
    parser = YamlParser()
    test = parser.load(Path("docs/examples/sample-test.yaml"))
    executor = TestExecutor()
    success = await executor.execute(test)

    assert success is True