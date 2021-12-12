import typing as t
from time import sleep

EXAMPLES = """start-A
start-b
A-c
A-b
b-d
A-end
b-end""".split("\n")


class Graph:
    def __init__(self):
        self.nodes = []

    def __repr__(self):
        return f"<Graph {self.nodes}>"

    def add_node(self, point_a: str, point_b: str):
        self.nodes.append((point_a, point_b))

    def make_paths(
        self, start: str, end: str, visited: t.Dict[str, bool], path_counts: t.List[int]
    ) -> None:
        if visited is None:
            visited = {}

        if not start.isupper():
            # Uppercase path can be visited many times, while lowercase can only be visited once
            visited[start] = True

        if start == end:
            path_counts[0] += 1
        else:
            for node in self.nodes:
                if node[0] == start and not visited[node[1]]:
                    self.make_paths(node[1], end, visited, path_counts)
                elif node[1] == start and not visited[node[0]]:
                    self.make_paths(node[0], end, visited, path_counts)

        visited[start] = False

    def make_paths_2(
        self, start: str, end: str, visited: t.Dict[str, bool], path_counts: t.List[int]
    ) -> None:
        if visited is None:
            visited = {}

        if not start.upper():
            if len(start) == 1 and start in visited:
                visited[start] = [True, True]
            elif len(start) == 1 and start not in visited:
                visited[start] = [True, False]
            else:
                visited[start] = [True]

        print(start, end, all(visited[start]), visited[start])
        sleep(1.0)

        if start == end:
            path_counts[0] += 1
            print(path_counts)
        else:
            for node in self.nodes:
                if node[0] == start and not all(visited[node[1]]):
                    self.make_paths_2(node[1], end, visited, path_counts)
                elif node[1] == start and not all(visited[node[0]]):
                    self.make_paths_2(node[0], end, visited, path_counts)

        visited[start] = [False, False]

    def possible_path(self, start: str, end: str):
        visited = {}
        for node in self.nodes:
            visited[node[0]] = False
            visited[node[1]] = False

        path_counts = [0]
        self.make_paths(start, end, visited, path_counts)
        return path_counts[0]

    def possible_path_2(self, start: str, end: str):
        visited = {}
        for node in self.nodes:
            visited[node[0]] = [False, False]
            visited[node[1]] = [False, False]

        path_counts = [0]
        self.make_paths_2(start, end, visited, path_counts)
        return path_counts[0]


# Part A
def part_a(input_strings: t.List[str]) -> int:
    g = Graph()
    for paths in input_strings:
        g.add_node(*paths.split("-"))

    return g.possible_path("start", "end")


# Part B
def part_b(input_strings: t.List[str]) -> int:
    g = Graph()
    for paths in input_strings:
        g.add_node(*paths.split("-"))

    return g.possible_path_2("start", "end")


if __name__ == "__main__":
    in_data = [num.rstrip() for num in open("input", "r").readlines() if num]

    print(f"Part A: {part_a(in_data)}")
    # print(f"Part B: {part_b(EXAMPLES)}")
