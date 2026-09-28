from pathlib import Path
from src.application.parsers.yaml_parser import YamlParser


def test_yaml_parser():
    parser = YamlParser()
    test = parser.load(Path("docs/examples/sample-test.yaml"))

    assert test.name == "Login Test"
    assert len(test.steps) > 0

