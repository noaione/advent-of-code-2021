import typing as t


EXAMPLES = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526""".split("\n")


# Part A
def part_a(input_strings: t.List[str]) -> int:
    return 0


# Part B
def part_b(input_strings: t.List[str]) -> int:
    return 0


if __name__ == "__main__":
    in_data = [num.rstrip() for num in open("input", "r").readlines() if num]

    print(f"Part A: {part_a(EXAMPLES)}")
    print(f"Part B: {part_b(in_data)}")
