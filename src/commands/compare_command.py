from src.commands.base_command import BaseCommand


class CompareCommand(BaseCommand):

    def __init__(
        self,
        left: str,
        right: str
    ):
        self.left = left
        self.right = right

    async def execute(self) -> None:

        if self.left != self.right:
            raise ValueError(
                f"{self.left} != {self.right}"
            )