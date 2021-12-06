# Part A and B
# using dict
def solve(input_string: str, max_day: int) -> int:
    fishy = {i: 0 for i in range(9)}
    for data in map(int, input_string.split(",")):
        fishy[data] += 1

    for _ in range(max_day):
        new_fishy = {i: 0 for i in range(9)}
        for i in fishy.keys():
            if i == 0:
                new_fishy[6] += fishy[0]
                new_fishy[8] += fishy[0]
            else:
                new_fishy[i - 1] += fishy[i]
        fishy = new_fishy.copy()

    return sum(fishy.values())


if __name__ == "__main__":
    in_data = [num.rstrip() for num in open("input", "r").readlines() if num][0]

    print(f"Part A: {solve(in_data, 80)}")
    print(f"Part B: {solve(in_data, 256)}")
