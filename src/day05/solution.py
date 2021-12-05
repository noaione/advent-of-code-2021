import typing as t
from dataclasses import dataclass


@dataclass
class Path:
    x0: int
    y0: int
    x1: int
    y1: int


def parse_path(input_strings: t.List[str]) -> t.List[Path]:
    all_paths = []
    for path in input_strings:
        x1y1, x2y2 = path.split(" -> ")
        x1, y1 = x1y1.split(",")
        x2, y2 = x2y2.split(",")
        all_paths.append(Path(int(x1), int(y1), int(x2), int(y2)))
    return all_paths


# Part A
def part_a(paths: t.List[Path]) -> int:
    matrixes: t.List[t.List[int]] = []

    min_x = 0
    min_y = 0

    max_x0 = max(path.x0 for path in paths)
    max_x1 = max(path.x1 for path in paths)
    max_x = max(max_x0, max_x1)

    max_y0 = max(path.y0 for path in paths)
    max_y1 = max(path.y1 for path in paths)
    max_y = max(max_y0, max_y1)

    for _ in range(min_x, max_x + 1):
        matrixes.append([0 for _ in range(min_y, max_y + 1)])

    for path in paths:
        if path.x0 == path.x1:
            step = 1 if path.y0 < path.y1 else -1
            for y in range(path.y0, path.y1 + step, step):
                matrixes[y][path.x0] += 1
        elif path.y0 == path.y1:
            step = 1 if path.x0 < path.x1 else -1
            for x in range(path.x0, path.x1 + step, step):
                matrixes[path.y0][x] += 1

    # Find number that are 2 or more
    return sum(sum(1 for x in row if x >= 2) for row in matrixes)


# Part B
def part_b(paths: t.List[Path]) -> int:
    matrixes: t.List[t.List[int]] = []

    min_x = 0
    min_y = 0

    max_x0 = max(path.x0 for path in paths)
    max_x1 = max(path.x1 for path in paths)
    max_x = max(max_x0, max_x1)

    max_y0 = max(path.y0 for path in paths)
    max_y1 = max(path.y1 for path in paths)
    max_y = max(max_y0, max_y1)

    for _ in range(min_x, max_x + 1):
        matrixes.append([0 for _ in range(min_y, max_y + 1)])

    for path in paths:
        if path.x0 == path.x1:
            step = 1 if path.y0 < path.y1 else -1
            for y in range(path.y0, path.y1 + step, step):
                matrixes[y][path.x0] += 1
        elif path.y0 == path.y1:
            step = 1 if path.x0 < path.x1 else -1
            for x in range(path.x0, path.x1 + step, step):
                matrixes[path.y0][x] += 1
        elif abs(path.x1 - path.x0) == abs(path.y1 - path.y0):
            step_x = 1 if path.x0 < path.x1 else -1
            step_y = 1 if path.y0 < path.y1 else -1
            for x, y in zip(
                range(path.x0, path.x1 + step_x, step_x),
                range(path.y0, path.y1 + step_y, step_y)
            ):
                matrixes[y][x] += 1

    # Find number that are 2 or more
    return sum(sum(1 for x in row if x >= 2) for row in matrixes)


if __name__ == "__main__":
    in_data = [num.rstrip() for num in open("input", "r").readlines()]

    paths = parse_path(in_data)
    print(f"Part A: {part_a(paths)}")
    print(f"Part B: {part_b(paths)}")
