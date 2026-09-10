from src.commands.base_command import BaseCommand


class LogCommand(BaseCommand):

    def __init__(self, message: str):
        self.message = message

    async def execute(self) -> None:
        print(self.message)