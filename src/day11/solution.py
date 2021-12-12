import typing as t


# Part A
def part_a(input_strings: t.List[str], steps: int = 100) -> int:
    octopus_grids = []
    for input_string in input_strings:
        octopus_grids.append(list(map(int, list(input_string))))

    flashed_octopuses = 0
    for _ in range(steps):
        octopus_copy = octopus_grids[:]
        flashing_index = []
        for index_y, grid_y in enumerate(octopus_grids):
            for index_x, grid_x in enumerate(grid_y):
                octopus_copy[index_y][index_x] += 1
                if grid_x + 1 > 9:
                    octopus_copy[index_y][index_x] = 0
                    flashed_octopuses += 1
                    flashing_index.append((index_y, index_x))

        for index_y, index_x in flashing_index:
            # Add 1 to any adjacent index
            update_grids = [
                (index_y - 1, index_x - 1), (index_y - 1, index_x), (index_y - 1, index_x + 1),
                (index_y, index_x - 1), (index_y, index_x + 1),
                (index_y + 1, index_x - 1), (index_y + 1, index_x), (index_y + 1, index_x + 1)
            ]
            # Remove any out of bounds
            update_grids = [
                (index_y, index_x) for (index_y, index_x) in update_grids if
                (0 <= index_y < len(octopus_copy)) and (0 <= index_x < len(octopus_copy[index_y]))
                and (index_y, index_x) not in flashing_index
            ]
            for upd_y, upd_x in update_grids:
                octopus_copy[upd_y][upd_x] += 1
                if octopus_copy[upd_y][upd_x] > 9:
                    octopus_copy[upd_y][upd_x] = 0
                    flashed_octopuses += 1
                    flashing_index.append((upd_y, upd_x))

        octopus_grids = octopus_copy

    return flashed_octopuses


# Part B
def part_b(input_strings: t.List[str]) -> int:
    octopus_grids = []
    for input_string in input_strings:
        octopus_grids.append(list(map(int, list(input_string))))

    flashed_octopuses = 0
    found_index = None
    steps = 0
    while found_index is None:
        octopus_copy = octopus_grids[:]
        flashing_index = []
        for index_y, grid_y in enumerate(octopus_grids):
            for index_x, grid_x in enumerate(grid_y):
                octopus_copy[index_y][index_x] += 1
                if grid_x + 1 > 9:
                    octopus_copy[index_y][index_x] = 0
                    flashed_octopuses += 1
                    flashing_index.append((index_y, index_x))

        for index_y, index_x in flashing_index:
            # Add 1 to any adjacent index
            update_grids = [
                (index_y - 1, index_x - 1), (index_y - 1, index_x), (index_y - 1, index_x + 1),
                (index_y, index_x - 1), (index_y, index_x + 1),
                (index_y + 1, index_x - 1), (index_y + 1, index_x), (index_y + 1, index_x + 1)
            ]
            # Remove any out of bounds
            update_grids = [
                (index_y, index_x) for (index_y, index_x) in update_grids if
                (0 <= index_y < len(octopus_copy)) and (0 <= index_x < len(octopus_copy[index_y]))
                and (index_y, index_x) not in flashing_index
            ]
            for upd_y, upd_x in update_grids:
                octopus_copy[upd_y][upd_x] += 1
                if octopus_copy[upd_y][upd_x] > 9:
                    octopus_copy[upd_y][upd_x] = 0
                    flashed_octopuses += 1
                    flashing_index.append((upd_y, upd_x))

        # Check all grids if it's flashing
        all_found = True
        for index_y, grid_y in enumerate(octopus_grids):
            for index_x, grid_x in enumerate(grid_y):
                check_index = (index_y, index_x)
                if check_index not in flashing_index:
                    all_found = False
                    break
        steps += 1

        if all_found:
            found_index = steps
            break

        octopus_grids = octopus_copy

    return found_index


if __name__ == "__main__":
    in_data = [num.rstrip() for num in open("input", "r").readlines() if num]

    print(f"Part A: {part_a(in_data)}")
    print(f"Part B: {part_b(in_data)}")
