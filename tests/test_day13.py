import sys
from pathlib import Path

current_path = Path(__file__).absolute().parent.parent
source_dir = current_path / "src"
sys.path.insert(0, str(source_dir))

from day13.solution import solve  # noqa

EXAMPLES = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
""".split("\n")
EXAMPLES = [num.rstrip() for num in EXAMPLES if num]


def test_solve_fold_single():
    assert solve(EXAMPLES) == 17


def test_solve_fold_all():
    assert solve(EXAMPLES, -1) == 16
