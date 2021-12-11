import typing as t


# Part A
def part_a(input_strings: t.List[str]) -> int:
    return 0


# Part B
def part_b(input_strings: t.List[str]) -> int:
    return 0


if __name__ == "__main__":
    in_data = [num.rstrip() for num in open("input", "r").readlines() if num]

    print(f"Part A: {part_a(in_data)}")
    print(f"Part B: {part_b(in_data)}")
