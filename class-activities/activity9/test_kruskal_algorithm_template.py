import unittest
from example_022_minimum_spanning_tree_Kruskal_algo import Graph, Edge, Vertex


class TestKruskalAlgorithm(unittest.TestCase):

    def setUp(self):
        # Create your Test Graphs here.
        test_graph = Graph(7)

        test_graph.add_edge(0, 1, 30)
        test_graph.add_edge(0, 6, 10)
        test_graph.add_edge(1, 4, 13)
        test_graph.add_edge(1, 2, 15)
        test_graph.add_edge(2, 3, 12)
        test_graph.add_edge(3, 4, 16)
        test_graph.add_edge(3, 5, 20)
        test_graph.add_edge(4, 5, 21)
        test_graph.add_edge(5, 6, 22)

        disconnected_graph = Graph(5)

        disconnected_graph.add_edge(0, 1, 10)
        disconnected_graph.add_edge(1, 2, 5)
        disconnected_graph.add_edge(3, 4, 10)

        self.disconnected_graph = disconnected_graph
        self.empty_graph = Graph(0)
        self.single_vertex = Graph(1)
        self.test_graph = test_graph

    def test_kruskal_mst(self):
        # Compute the minimum spanning tree using Kruskal's algorithm
        expected_mst = [
            Edge(start=Vertex(0), end=Vertex(6), weight=10),
            Edge(start=Vertex(2), end=Vertex(3), weight=12),
            Edge(start=Vertex(1), end=Vertex(4), weight=13),
            Edge(start=Vertex(1), end=Vertex(2), weight=15),
            Edge(start=Vertex(3), end=Vertex(5), weight=20),
            Edge(start=Vertex(5), end=Vertex(6), weight=22)
        ]

        result_mst = self.test_graph.kruskal_mst()

        for edge in expected_mst:
            self.assertIn(edge, result_mst)

    def test_kruskal_mst_empty_graph(self):
        mst = self.empty_graph.kruskal_mst()
        self.assertEqual(len(mst), 0)

    def test_kruskal_mst_single_vertex(self):
        mst = self.single_vertex.kruskal_mst()
        self.assertEqual(len(mst), 1)

    def test_kruskal_mst_disconnected_graph(self):
        expected_mst = [
            Edge(start=Vertex(1), end=Vertex(2), weight=5),
            Edge(start=Vertex(0), end=Vertex(1), weight=10),
            Edge(start=Vertex(3), end=Vertex(4), weight=10),
        ]

        result_mst = self.disconnected_graph.kruskal_mst()

        for edge in expected_mst:
            self.assertIn(edge, result_mst)


if __name__ == '__main__':
    unittest.main()
