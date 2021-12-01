in_data = [int(num.rstrip()) for num in open("input", "r").readlines() if num]

# Part A
prev = in_data[0]
part_a = 0
for num in in_data[1:]:
    if num > prev:
        part_a += 1
    prev = num
print(f"Part A: {part_a}")

# Part B
part_b = 0
for i in range(0, len(in_data) - 2):
    if in_data[i + 2] > in_data[i - 1]:
        part_b += 1

print(f"Part B: {part_b}")
