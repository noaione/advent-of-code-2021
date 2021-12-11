import sys
from pathlib import Path

import pytest

current_path = Path(__file__).absolute().parent.parent
source_dir = current_path / "src"
sys.path.insert(0, str(source_dir))

from day11.solution import part_a, part_b  # noqa

EXAMPLES = """
""".split("\n")


@pytest.mark.skip(reason="Part A is not implemented yet")
def test_part_a_solution():
    assert part_a(EXAMPLES) == 0


@pytest.mark.skip(reason="Part B is not implemented yet")
def test_part_b_solution():
    assert part_b(EXAMPLES) == 0
