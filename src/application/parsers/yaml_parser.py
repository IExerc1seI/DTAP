from pathlib import Path
from uuid import uuid4

import yaml

from src.domain.entities.test import Test
from src.domain.entities.test_step import TestStep


class YamlParser:
    def load(self, path: Path) -> Test:
        with path.open(encoding="utf-8") as fh:
            data = yaml.safe_load(fh)

        required_fields = [
            "name",
            "description",
            "steps",
        ]

        missing_fields = [
            field
            for field in required_fields
            if not data.get(field)
        ]

        if missing_fields:
            raise ValueError(
                f"Missing required fields: {', '.join(missing_fields)}"
            )

        test = Test(
            name=data["name"],
            description=data["description"],
        )

        for order, step_data in enumerate(data["steps"], start=1):
            action = step_data.get("action")

            if not action:
                raise ValueError(
                    f"Step #{order} is missing 'action' field"
                )

            parameters = {
                key: value
                for key, value in step_data.items()
                if key != "action"
            }

            step = TestStep(
                id=uuid4(),
                action=action,
                parameters=parameters,
                order=order,
            )

            test.add_step(step)

        return test