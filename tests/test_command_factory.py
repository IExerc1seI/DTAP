from src.application.factories.command_factory import CommandFactory
from src.domain.entities.test_step import TestStep

def test_command_factory():
    step = TestStep(action="log", parameters={"message": "Hello"}, order=1)
    command = CommandFactory.create(step)

    assert command.__class__.__name__ == "LogCommand"