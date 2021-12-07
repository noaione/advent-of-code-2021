import typing as t


# Part A
def part_a(input_string: str) -> int:
    crabs = list(map(int, input_string.split(",")))
    possibilites: t.Dict[int, int] = {}

    max_pos = max(crabs)
    for i in range(1, max_pos + 1):
        possibilites[i] = 0

    for i in possibilites:
        for j in crabs:
            move = abs(j - i)
            possibilites[i] += move
    return min(possibilites.values())


# Part B
def part_b(input_string: str) -> int:
    crabs = list(map(int, input_string.split(",")))
    possibilites: t.Dict[int, int] = {}

    max_pos = max(crabs)
    for i in range(1, max_pos + 1):
        possibilites[i] = 0

    for i in possibilites:
        for j in crabs:
            move = abs(j - i)
            possibilites[i] += move * (move + 1) // 2
    return min(possibilites.values())


if __name__ == "__main__":
    in_data = [num.rstrip() for num in open("input", "r").readlines() if num][0]

    print(f"Part A: {part_a(in_data)}")
    print(f"Part B: {part_b(in_data)}")
