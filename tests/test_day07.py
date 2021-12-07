import sys
from pathlib import Path

current_path = Path(__file__).absolute().parent.parent
source_dir = current_path / "src"
sys.path.insert(0, str(source_dir))

from day07.solution import part_a, part_b, step_number  # noqa

EXAMPLES = "16,1,2,0,4,2,7,1,2,14"


def test_part_a_solution():
    assert part_a(EXAMPLES) == 37


def test_part_b_solution():
    assert part_b(EXAMPLES) == 168


def test_number_stepping():
    assert step_number(0) == 0
    assert step_number(1) == 1
    assert step_number(2) == 3
    assert step_number(3) == 6
