import typing as t

# Part B answer
# [
#     [1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0],  # noqa
#     [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0],  # noqa
#     [1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],  # noqa
#     [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],  # noqa
#     [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0],  # noqa
#     [1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0]  # noqa
# ]


def solve(input_strings: t.List[str], fold_count: int = 1) -> int:
    positions: t.List[t.Tuple[int, int]] = []
    folding_instructions: t.List[str] = []
    matrixes: t.List[t.List[t.List[int]]] = []
    min_x = 0
    min_y = 0
    max_x = 0
    max_y = 0

    for input_string in input_strings:
        if input_string.strip() == "":
            continue
        if input_string.startswith("fold along "):
            input_string = input_string.replace("fold along ", "")
            method, value = input_string.split("=")
            value = int(value)
            folding_instructions.append((method, value))
        else:
            x, y = input_string.split(",")
            x = int(x)
            y = int(y)
            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y
            positions.append((x, y))

    for _ in range(min_y, max_y + 1):
        matrixes.append([0 for _ in range(min_x, max_x + 1)])

    for x_mark, y_mark in positions:
        matrixes[y_mark][x_mark] = 1

    # pprint.pprint(matrixes)
    current_fold = 0
    for fold, value in folding_instructions:
        if fold_count != -1 and current_fold >= fold_count:
            break
        if fold == "y":
            matrix_top, matrix_bottom = matrixes[:][:value], matrixes[:][value + 1:]
            matrix_bottom.reverse()

            bot_copy = matrix_bottom[:]
            top_copy = matrix_top[:]
            final_copy = matrix_top[:]

            for y in range(len(top_copy)):
                for x in range(len(top_copy[y])):
                    value = int(bot_copy[y][x])
                    another_value = int(top_copy[y][x])
                    merge_value = value or another_value
                    final_copy[y][x] = merge_value
            matrixes = final_copy[:]
            del bot_copy
            del top_copy
        elif fold == "x":
            copy_matrix = matrixes[:]

            left_side = []
            right_side = []
            for y in range(len(copy_matrix)):
                left_side.append(copy_matrix[y][:value])
                right_side.append(copy_matrix[y][value + 1:])

            reversed_right_side = []
            for row in right_side:
                reversed_right_side.append(row[::-1])

            final_copy = left_side[:]

            for y in range(len(left_side)):
                for x in range(len(left_side[y])):
                    value = int(left_side[y][x])
                    another_value = int(reversed_right_side[y][x])
                    merge_value = value or another_value
                    final_copy[y][x] = merge_value
            matrixes = final_copy[:]
            del left_side
            del right_side
        current_fold += 1

    if fold_count == -1:
        for row in matrixes:
            for value in row:
                if value == 1:
                    print("#", end="")
                else:
                    print(" ", end="")
            print()

    # Count the number of 1s
    return sum(map(sum, matrixes))


if __name__ == "__main__":
    in_data = [num.rstrip() for num in open("input", "r").readlines() if num]

    print(f"Part A: {solve(in_data)}")
    print(f"Part B: {solve(in_data, -1)}")
