import typing as t


def flip_bits(bits: str) -> str:
    return bits.replace("0", "2").replace("1", "0").replace("2", "1")


def part_a(binary_lines: t.List[str]) -> int:
    max_len = len(binary_lines[0])
    gamma = ""
    for col in range(max_len):
        current = {"0": 0, "1": 0}
        for line in binary_lines:
            if line[col] not in current:
                current[line[col]] = 1
                continue
            current[line[col]] += 1
        if current["0"] > current["1"]:
            gamma += "0"
        else:
            gamma += "1"
    return int(gamma, 2) * int(flip_bits(gamma), 2)


def select_lines(current: t.Dict[str, t.List[str]], reverse: bool = False) -> t.List[str]:
    zero = current.get("0", [])
    one = current.get("1", [])
    if len(zero) > len(one):
        return zero if not reverse else one
    return one if not reverse else zero


def part_b(binary_lines: t.List[str]) -> int:
    max_len = len(binary_lines[0])
    gamma = ""
    epsilon = ""
    check_lines = binary_lines.copy()
    check_lines_epsilon = binary_lines.copy()
    for col in range(max_len):
        current: t.Dict[str, t.List[str]] = {"0": [], "1": []}
        current_epsilon: t.Dict[str, t.List[str]] = {"0": [], "1": []}
        for line in check_lines:
            current[line[col]].append(line)
        for line in check_lines_epsilon:
            current_epsilon[line[col]].append(line)
        if len(check_lines) > 1:
            check_lines = select_lines(current)
        if len(check_lines_epsilon) > 1:
            check_lines_epsilon = select_lines(current_epsilon, True)
        gamma = check_lines[0]
        epsilon = check_lines_epsilon[0]
    return int(gamma, 2) * int(epsilon, 2)


# Answers
if __name__ == "__main__":
    in_data = [num.rstrip() for num in open("input", "r").readlines() if num]
    print(f"Part A: {part_a(in_data)}")
    print(f"Part B: {part_b(in_data)}")
