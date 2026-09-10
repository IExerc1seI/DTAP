from src.commands.log_command import LogCommand
from src.commands.wait_command import WaitCommand
from src.commands.fail_command import FailCommand
from src.commands.compare_command import CompareCommand

from src.domain.entities.test_step import TestStep


class CommandFactory:

    @staticmethod
    def create(step: TestStep):

        match step.action:

            case "log":
                return LogCommand(
                    message=step.parameters["message"]
                )

            case "wait":
                return WaitCommand(
                    seconds=step.parameters["seconds"]
                )

            case "fail":
                return FailCommand()

            case "compare":
                return CompareCommand(
                    left=step.parameters["left"],
                    right=step.parameters["right"]
                )

            case _:
                raise ValueError(
                    f"Unsupported action: {step.action}"
                )