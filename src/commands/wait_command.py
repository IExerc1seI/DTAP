import asyncio

from src.commands.base_command import BaseCommand


class WaitCommand(BaseCommand):

    def __init__(self, seconds: int):
        self.seconds = seconds

    async def execute(self) -> None:
        await asyncio.sleep(self.seconds)