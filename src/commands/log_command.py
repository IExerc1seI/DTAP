from src.commands.base_command import BaseCommand
from src.infrastructure.logging import logger

class LogCommand(BaseCommand):

    def __init__(self, message: str):
        self.message = message

    async def execute(self) -> None:
        logger.info(self.message)
    