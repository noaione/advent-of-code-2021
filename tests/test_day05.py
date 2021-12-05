import sys
from pathlib import Path

current_path = Path(__file__).absolute().parent.parent
source_dir = current_path / "src"
sys.path.insert(0, str(source_dir))

from day05.solution import part_a, part_b, parse_path, Path as Day5Path  # noqa

EXAMPLES = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2""".split("\n")


def test_parse_path():
    expect = Day5Path(0, 9, 5, 0)
    assert parse_path(["0,9 -> 5,0"])[0] == expect


def test_part_a_solution():
    paths = parse_path(EXAMPLES)
    assert part_a(paths) == 5


def test_part_b_solution():
    paths = parse_path(EXAMPLES)
    assert part_b(paths) == 12
