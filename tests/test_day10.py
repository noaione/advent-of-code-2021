import sys
from pathlib import Path

current_path = Path(__file__).absolute().parent.parent
source_dir = current_path / "src"
sys.path.insert(0, str(source_dir))

from day10.solution import part_a, part_b  # noqa

EXAMPLES = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]""".split("\n")


def test_part_a_solution():
    assert part_a(EXAMPLES) == 26397


def test_part_b_solution():
    assert part_b(EXAMPLES) == 288957
