import sys
from pathlib import Path

import pytest

current_path = Path(__file__).absolute().parent.parent
source_dir = current_path / "src"
sys.path.insert(0, str(source_dir))

from day12.solution import part_a, part_b  # noqa

EXAMPLES = """start-A
start-b
A-c
A-b
b-d
A-end
b-end""".split("\n")


def test_part_a_solution():
    assert part_a(EXAMPLES) == 10


@pytest.mark.skip(reason="Not implemented/incomplete")
def test_part_b_solution():
    assert part_b(EXAMPLES) == 0
