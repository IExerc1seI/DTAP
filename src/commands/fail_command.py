from src.commands.base_command import BaseCommand


class FailCommand(BaseCommand):

    async def execute(self) -> None:
        raise RuntimeError(
            "Command failed intentionally."
        )