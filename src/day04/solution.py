from __future__ import annotations

import typing as t


class Board:
    def __init__(self, board_id: str, rows: t.List[t.List[int]]):
        # Custom id to check later
        self._id = board_id
        self.rows: t.List[t.List[int]] = rows
        self.marker: t.List[t.List[bool]] = [
            [False, False, False, False, False],
            [False, False, False, False, False],
            [False, False, False, False, False],
            [False, False, False, False, False],
            [False, False, False, False, False],
        ]

    def __int__(self):
        return len(self.rows)

    def __eq__(self, other: t.Union[Board, int, str]) -> bool:
        if isinstance(other, Board):
            return self._id == other._id
        elif isinstance(other, (str, int)):
            return str(other) == self._id
        return False

    def __repr__(self):
        return "<Board {}>".format(self.rows[0])

    def play(self, number: int):
        for row in range(len(self.rows)):
            for col in range(len(self.rows[row])):
                if self.rows[row][col] == number:
                    self.marker[row][col] = True

    def _check_col(self) -> bool:
        for col in range(5):
            marker = []
            for row in range(5):
                marker.append(self.marker[row][col])
            if all(marker):
                return True
        return False

    def _check_row(self) -> bool:
        for rows in enumerate(self.marker):
            if all(rows):
                return True
        return False

    def check(self) -> bool:
        if self._check_row() is not None:
            return True
        if self._check_col() is not None:
            return True
        return False

    def sum_of_non_winning(self):
        sum_of_non_winning = 0
        for row in range(5):
            for col in range(5):
                if not self.marker[row][col]:
                    sum_of_non_winning += self.rows[row][col]
        return sum_of_non_winning


def parse_board(input_strings: t.List[str]) -> t.Tuple[t.List[Board], t.List[int]]:
    # Returns the [Board], and play order
    game_order = list(map(int, input_strings[0].split(",")))
    boards: t.List[Board] = []
    current_boards = []
    for board in input_strings[1:]:
        if board == "" and current_boards:
            boards.append(Board(f"{current_boards!r}", current_boards))
            current_boards = []
            continue
        split_board = [int(x) for x in board.split(" ") if x]
        if split_board:
            current_boards.append(split_board)
    if current_boards:
        boards.append(Board(f"{current_boards!r}", current_boards))
    return boards, game_order


# Part A
def part_a(boards: t.List[Board], play_order: t.List[int]) -> int:
    winning_board: Board = None
    winning_play: int = None
    for move in play_order:
        if winning_board is not None:
            break
        for board in boards:
            board.play(move)
            if board.check():
                winning_board = board
                winning_play = move
                break

    sum_of_non_win = winning_board.sum_of_non_winning()
    return winning_play * sum_of_non_win


# Part B
def part_b(boards: t.List[Board], play_order: t.List[int]) -> int:
    winning_board: t.List[Board] = []
    winning_play: t.List[int] = []
    for move in play_order:
        if len(winning_board) == len(boards):
            break
        for board in boards:
            if board in winning_board:
                continue
            board.play(move)
            if board.check():
                winning_board.append(board)
                winning_play.append(move)
    return winning_board[-1].sum_of_non_winning() * winning_play[-1]


if __name__ == "__main__":
    in_data = [num.rstrip() for num in open("input", "r").readlines()]
    boards, game_order = parse_board(in_data)

    print(f"Part A: {part_a(boards, game_order)}")
    print(f"Part B: {part_b(boards, game_order)}")
