from src.application.factories.command_factory import CommandFactory
from src.domain.entities.test import Test

class TestExecutor:

    async def execute(self,test:Test) -> bool:
        try:
            for step in test.steps:
                command = CommandFactory.create(step)
                await command.execute()
            return True

        except Exception as error:
            print(f"Execution failed: {error}")
            return False