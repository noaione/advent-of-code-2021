import sys
from pathlib import Path

current_path = Path(__file__).absolute().parent.parent
source_dir = current_path / "src"
sys.path.insert(0, str(source_dir))

from day06.solution import solve  # noqa


def test_solve_solution():
    assert solve("3,4,3,1,2", 4) == 9
