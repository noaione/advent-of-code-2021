import sys
from pathlib import Path

current_path = Path(__file__).absolute().parent.parent
source_dir = current_path / "src"
sys.path.insert(0, str(source_dir))

from day02.solution import part_a, part_b  # noqa

EXAMPLES = """forward 5
down 5
forward 8
up 3
down 8
forward 2""".split("\n")


def test_part_a_solution():
    assert part_a(EXAMPLES) == 150


def test_part_b_solution():
    assert part_b(EXAMPLES) == 900
