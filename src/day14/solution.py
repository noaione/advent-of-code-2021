import typing as t
from collections import Counter


# Part A
def solve(input_strings: t.List[str], steps: int) -> int:
    template = input_strings[0]
    chains = {}
    for chain in input_strings[1:]:
        pair, inject = chain.split(" -> ")
        chains[pair] = [pair[0] + inject, inject + pair[1]]

    freqs = Counter()
    for a, b in zip(template, template[1:]):
        c = a + b
        freqs[c] += 1

    counts = Counter(template)
    for _ in range(steps):
        step_count = Counter()
        for pair, count in freqs.items():
            if pair in chains:
                counts[chains[pair][0][1]] += count
                for inject in chains[pair]:
                    step_count[inject] += count

        freqs = step_count
    uniques = counts.most_common()
    return uniques[0][1] - uniques[-1][1]


if __name__ == "__main__":
    in_data = [num.rstrip() for num in open("input", "r").readlines() if num.rstrip()]

    print(f"Part A: {solve(in_data, 10)}")
    print(f"Part B: {solve(in_data, 40)}")
