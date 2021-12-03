import typing as t


# Part A
def part_a(contents: t.List[str]) -> int:
    total = 0
    for i in range(1, len(contents)):
        if contents[i] > contents[i - 1]:
            total += 1
    return total


# Part B
def part_b(contents: t.List[str]) -> int:
    total = 0
    for i in range(0, len(contents) - 2):
        if contents[i + 2] > contents[i - 1]:
            total += 1
    return total


if __name__ == "__main__":
    in_data = [int(num.rstrip()) for num in open("input", "r").readlines() if num]

    print(f"Part A: {part_a(in_data)}")
    print(f"Part B: {part_b(in_data)}")
