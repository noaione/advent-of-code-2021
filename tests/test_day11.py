import sys
from pathlib import Path

current_path = Path(__file__).absolute().parent.parent
source_dir = current_path / "src"
sys.path.insert(0, str(source_dir))

from day11.solution import part_a, part_b  # noqa

EXAMPLES = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526""".split("\n")


def test_part_a_solution():
    assert part_a(EXAMPLES) == 1656


def test_part_b_solution():
    assert part_b(EXAMPLES) == 195
