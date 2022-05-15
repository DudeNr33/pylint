# Licensed under the GPL: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html
# For details: https://github.com/PyCQA/pylint/blob/main/LICENSE
# Copyright (c) https://github.com/PyCQA/pylint/blob/main/CONTRIBUTORS.txt

from pathlib import Path

import pytest

from pylint.testutils import pyreverse

HERE = Path(__file__).parent
DATA_DIRECTORY = HERE / "data" / "pyreverse"


def test_testoptions_with_pythonpath() -> None:
    functional_test_file = pyreverse.get_functional_test_files(
        root_directory=DATA_DIRECTORY / "pythonpath_option"
    )[0]
    assert functional_test_file.options["pythonpath"] == str(HERE / "data")


def test_testoptions_with_output_formats() -> None:
    functional_test_file = pyreverse.get_functional_test_files(
        root_directory=DATA_DIRECTORY / "output_formats_option"
    )[0]
    assert functional_test_file.options["output_formats"] == ["dot", "png"]


def test_testoptions_with_command_line_args() -> None:
    functional_test_file = pyreverse.get_functional_test_files(
        root_directory=DATA_DIRECTORY / "command_line_args_option"
    )[0]
    assert functional_test_file.options["command_line_args"] == ["-ASmy"]


@pytest.mark.parametrize("input_folder", ["empty_rcfile", "no_rcfile"])
def test_default_values(input_folder: str) -> None:
    functional_test_file = pyreverse.get_functional_test_files(
        root_directory=DATA_DIRECTORY / input_folder
    )[0]
    assert functional_test_file.options["output_formats"] == ["mmd"]
    assert functional_test_file.options["command_line_args"] == []
    assert functional_test_file.options["pythonpath"] is None
