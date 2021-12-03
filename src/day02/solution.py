from typing import List


# Part A
def part_a(input_strings: List[str]) -> int:
    x = y = 0
    for instruction in input_strings:
        move, distance = instruction.split(" ")
        distance = int(distance)
        if move == "forward":
            x += distance
        elif move == "down":
            y += distance
        elif move == "up":
            y -= distance
    return x * y


# Part B
def part_b(input_strings: List[str]) -> int:
    x = y = aim = 0
    for instruction in input_strings:
        move, distance = instruction.split(" ")
        distance = int(distance)
        if move == "up":
            aim -= distance
        elif move == "down":
            aim += distance
        elif move == "forward":
            x += distance
            y += aim * distance
    return x * y


if __name__ == "__main__":
    in_data = [num.rstrip() for num in open("input", "r").readlines() if num]
    print(f"Part A: {part_a(in_data)}")
    print(f"Part A: {part_b(in_data)}")
