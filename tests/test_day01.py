import sys
from pathlib import Path

current_path = Path(__file__).absolute().parent.parent
source_dir = current_path / "src"
sys.path.insert(0, str(source_dir))

from day01.solution import part_a, part_b  # noqa

EXAMPLES = """199
200
208
210
200
207
240
269
260
263""".split("\n")
EXAMPLES = [int(x) for x in EXAMPLES if x]


def test_part_a_solution():
    assert part_a(EXAMPLES) == 7


def test_part_b_solution():
    assert part_b(EXAMPLES) == 5
