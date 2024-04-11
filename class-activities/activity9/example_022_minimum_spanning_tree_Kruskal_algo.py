class Vertex:
    def __init__(self, label: int) -> None:
        self.label = label
        self.parent = self

    def __str__(self):
        return f'Label: {self.label}, Parent: {self.parent.label}'

    def __eq__(self, other: 'Vertex') -> bool:
        return self.label == other.label


class Edge:
    def __init__(self, start: Vertex, end: Vertex, weight: int) -> None:
        self.weight = weight
        self.start = start
        self.end = end

    def __lt__(self, other: 'Edge') -> bool:
        return self.weight < other.weight

    def __str__(self) -> str:
        return f'{self.start.label} - {self.end.label}, {self.weight}'

    def __eq__(self, other: 'Edge') -> bool:
        return self.start.label == other.start.label and self.end.label == other.end.label and self.weight == other.weight


class Graph:
    def __init__(self, num_vertices: int) -> None:
        self.vertices = [Vertex(i) for i in range(num_vertices)]
        self.edges: list[Edge] = []

    def add_edge(self, start: int, end: int, weight: int) -> None:
        start_vert = self.vertices[start]
        end_vert = self.vertices[end]

        edge = Edge(start_vert, end_vert, weight)
        self.edges.append(edge)

    def find(self, vertex: Vertex) -> Vertex:
        if vertex.parent != vertex:
            vertex.parent = self.find(vertex.parent)
        return vertex.parent

    def union(self, vertex1: Vertex, vertex2: Vertex) -> None:
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)
        root1.parent = root2

    def kruskal_mst(self) -> list[Edge]:
        sorted_edges = sorted(self.edges)
        mst = []
        num_edges_added = 0

        if len(self.vertices) == 1:
            return [self.vertices[0]]

        for edge in sorted_edges:
            if num_edges_added == len(self.vertices) - 1:
                break

            start_root = self.find(edge.start)
            end_root = self.find(edge.end)

            if start_root != end_root:
                mst.append(edge)
                self.union(start_root, end_root)
                num_edges_added += 1

        return mst


def main():
    # create the Graph object
    g1 = Graph(7)

    g1.add_edge(0, 1, 30)
    g1.add_edge(0, 6, 10)
    g1.add_edge(1, 4, 13)
    g1.add_edge(1, 2, 15)
    g1.add_edge(2, 3, 12)
    g1.add_edge(3, 4, 16)
    g1.add_edge(3, 5, 20)
    g1.add_edge(4, 5, 21)
    g1.add_edge(5, 6, 22)

    path = g1.kruskal_mst()
    for val in path:
        print(val)


if __name__ == "__main__":
    main()
