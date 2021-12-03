import sys
from pathlib import Path

current_path = Path(__file__).absolute().parent.parent
source_dir = current_path / "src"
sys.path.insert(0, str(source_dir))

from day03.solution import flip_bits, part_a, part_b, select_lines  # noqa

EXAMPLES = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010""".split("\n")


def test_part_a_solution():
    assert part_a(EXAMPLES) == 198


def test_part_b_solution():
    assert part_b(EXAMPLES) == 230


def test_flip_bits():
    assert flip_bits("10110") == "01001"


def test_select_lines():
    test_lines = {
        "0": ["00100", "11110", "10110", "10111", "10101", "01111"],
        "1": ["01111", "00111", "11100", "10000", "11001", "00010", "01010"],
    }
    assert select_lines(test_lines) == ["01111", "00111", "11100", "10000", "11001", "00010", "01010"]
    assert select_lines(test_lines, reverse=True) == ["00100", "11110", "10110", "10111", "10101", "01111"]


def test_select_lines_same():
    test_lines = {
        "0": ["00100", "11110", "10110", "10111", "10101", "01111"],
        "1": ["01111", "00111", "11100", "10000", "11001", "00010"],
    }
    assert select_lines(test_lines) == ["01111", "00111", "11100", "10000", "11001", "00010"]
    assert select_lines(test_lines, True) == ["00100", "11110", "10110", "10111", "10101", "01111"]
