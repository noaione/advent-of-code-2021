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


def step_number(number: int) -> int:
    # Example:
    # If we got the number 0 means we just need to return zero
    # If we got one, we return one since it only one move
    # If we got maybe three, we make it one + two + three which equals six

    final = 0
    for i in range(1, number + 1):
        final += i
    return final


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
            possibilites[i] += step_number(move)
    return min(possibilites.values())


if __name__ == "__main__":
    in_data = [num.rstrip() for num in open("input", "r").readlines() if num][0]
    examples = "16,1,2,0,4,2,7,1,2,14"

    print(f"Part A: {part_a(in_data)}")
    print(f"Part B: {part_b(in_data)}")
