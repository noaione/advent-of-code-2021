import typing as t


# Part A
def part_a(input_strings: t.List[str]) -> int:
    brackets_pair = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">"
    }
    invalid_stacks = []
    for string in input_strings:
        frame_stacks = []
        for x, char in enumerate(string):
            if char in brackets_pair.keys():
                frame_stacks.append(brackets_pair[char])
            elif char in brackets_pair.values():
                if len(frame_stacks) > 0:
                    if char == frame_stacks[-1]:
                        frame_stacks.pop()
                    else:
                        # print(f"Invalid string at index {x}: {string}")
                        invalid_stacks.append(char)
                        break

    points_map = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137
    }

    return sum([points_map[x] for x in invalid_stacks])


# Part B
def part_b(input_strings: t.List[str]) -> int:
    brackets_pair = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">"
    }
    incomplete_stacks = []
    for string in input_strings:
        frame_stacks = []
        error_out = False
        for x, char in enumerate(string):
            if char in brackets_pair.keys():
                frame_stacks.append(brackets_pair[char])
            elif char in brackets_pair.values():
                if len(frame_stacks) > 0:
                    if char == frame_stacks[-1]:
                        frame_stacks.pop()
                    else:
                        # print(f"Invalid string at index {x}: {string}")
                        error_out = True
                        break

        if not error_out:
            incomplete_stacks.append(string)

    points_map = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4
    }

    # Add the missing closing pair in the stacks
    completion_scoring = []
    for string in incomplete_stacks:
        frame_stacks = []
        error_out = False
        for x, char in enumerate(string):
            if char in brackets_pair.keys():
                frame_stacks.append(brackets_pair[char])
            elif char in brackets_pair.values():
                if char == frame_stacks[-1]:
                    frame_stacks.pop()
        frame_stacks.reverse()

        scoring = 0
        for stack in frame_stacks:
            scoring *= 5
            scoring += points_map[stack]
        completion_scoring.append(scoring)

    completion_scoring.sort()

    # Get middle result
    middle_index = len(completion_scoring) // 2
    return completion_scoring[middle_index]


if __name__ == "__main__":
    in_data = [num.rstrip() for num in open("input", "r").readlines() if num]

    print(f"Part A: {part_a(in_data)}")
    print(f"Part B: {part_b(in_data)}")
