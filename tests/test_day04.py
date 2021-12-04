import sys
from pathlib import Path

current_path = Path(__file__).absolute().parent.parent
source_dir = current_path / "src"
sys.path.insert(0, str(source_dir))

from day04.solution import part_a, part_b, parse_board  # noqa

EXAMPLES = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7""".split("\n")


def test_board_parse():
    boards, _ = parse_board(EXAMPLES)
    assert len(boards) == 3


def test_play_order_parse():
    actual_order = list(map(int, EXAMPLES[0].split(",")))
    _, play_order = parse_board(EXAMPLES)
    assert play_order == actual_order


def test_board_play():
    boards, _ = parse_board(EXAMPLES)
    boards[0].play(23)
    assert boards[0].marker[1][2] is True


def test_board_check():
    boards, _ = parse_board(EXAMPLES)
    boards[0].play(23)
    assert boards[0].check() is False
    boards[0].play(24)
    boards[0].play(4)
    boards[0].play(8)
    boards[0].play(2)
    assert boards[0].check() is True
    assert boards[0]._check_col() is False
    assert boards[0]._check_row() is True


def test_board_sum_unmarked():
    boards, _ = parse_board(EXAMPLES)
    boards[0].play(23)
    boards[0].play(24)
    assert boards[0].sum_of_unmarked() == 253


def test_part_a_solution():
    boards, game_order = parse_board(EXAMPLES)
    assert part_a(boards, game_order) == 4512


def test_part_b_solution():
    boards, game_order = parse_board(EXAMPLES)
    assert part_b(boards, game_order) == 1924
