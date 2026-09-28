from src.application.factories.command_factory import CommandFactory
from src.domain.entities.test import Test
from src.infrastructure.logging.logger import logger

class TestExecutor:

    async def execute(self,test:Test) -> bool:
        try:
            logger.info(f"Test started: {test.name}")
            for step in test.steps:
                command = CommandFactory.create(step)
                await command.execute()
            logger.info(f"Test '{test.name}' executed successfully.")
            return True
        
        except Exception as error:
            logger.error(f"Error executing test '{test.name}': {error}")
            return False