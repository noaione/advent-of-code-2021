import sys
from pathlib import Path

current_path = Path(__file__).absolute().parent.parent
source_dir = current_path / "src"
sys.path.insert(0, str(source_dir))

from day14.solution import solve  # noqa

EXAMPLES = """NNCB
CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
XX -> X""".split("\n")


def test_single_solution():
    assert solve(EXAMPLES, 1) == 1


def test_multi_solution():
    assert solve(EXAMPLES, 10) == 1588
