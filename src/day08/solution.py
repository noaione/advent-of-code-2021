import typing as t


# Part A
def part_a(input_strings: t.List[str]) -> int:
    only_includes = [2, 4, 3, 7]
    occurences = 0
    for input_string in input_strings:
        _, output = input_string.split(" | ")
        outputs = output.split(" ")
        occurences += len(list(filter(lambda x: len(x) in only_includes, outputs)))
    return occurences


# Part B
def part_b(input_strings: t.List[str]) -> int:
    sum_output = 0
    for input_string in input_strings:
        signal, output = input_string.split(" | ")
        signals = signal.split(" ")
        outputs = output.split(" ")

        mappings = ["" for _ in range(10)]
        signals = sorted(signals, key=len)
        for sig in signals:
            tra = len(sig)
            if tra == 2:
                mappings[1] = sig
            elif tra == 3:
                mappings[7] = sig
            elif tra == 4:
                mappings[4] = sig
            elif tra == 5:
                if all(s in sig for s in mappings[1]):
                    mappings[3] = sig
                elif sum(s in sig for s in mappings[4]) == 3:
                    mappings[5] = sig
                else:
                    mappings[2] = sig
            elif tra == 6:
                if all(s in sig for s in mappings[4]):
                    mappings[9] = sig
                elif all(s in sig for s in mappings[7]):
                    mappings[0] = sig
                else:
                    mappings[6] = sig
            else:
                mappings[8] = sig

        parsed = 0
        for j, n in enumerate(outputs[::-1]):
            for i in range(10):
                if all(s in n for s in mappings[i]) and len(mappings[i]) == len(n):
                    parsed += i * 10 ** j
                    break

        sum_output += parsed
    return sum_output


if __name__ == "__main__":
    in_data = [num.rstrip() for num in open("input", "r").readlines() if num]

    print(f"Part A: {part_a(in_data)}")
    print(f"Part B: {part_b(in_data)}")
