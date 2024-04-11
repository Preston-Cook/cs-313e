import unittest
from typing import List, Tuple
from example_023_minimum_spanning_tree_Prims_algo import Graph


class TestPrimsAlgorithm(unittest.TestCase):

    def setUp(self):
        self.graph1 = {
            0: [(1, 2), (2, 3)],
            1: [(0, 2), (2, 4), (3, 1)],
            2: [(0, 3), (1, 4), (3, 2)],
            3: [(1, 1), (2, 2)]
        }
        self.expected_output1 = [(0, 1), (1, 3), (3, 2)]

        self.graph2 = {
            0: [(1, 1), (2, 4)],
            1: [(0, 1), (2, 2), (3, 3)],
            2: [(0, 4), (1, 2), (3, 5)],
            3: [(1, 3), (2, 5)]
        }
        self.expected_output2 = [(0, 1), (1, 2), (1, 3)]

        self.graph3 = {
            0: [(1, 3), (2, 4)],
            1: [(0, 3), (2, 5), (3, 2)],
            2: [(0, 4), (1, 5), (3, 1)],
            3: [(1, 2), (2, 1)]
        }
        self.expected_output3 = [(0, 1), (1, 3), (3, 2)]

        # Create your Test Graphs here.
        self.test_graph1 = Graph()
        self.test_graph1.add_verticies(self.graph1.keys())

        for vertex, edges in self.graph1.items():
            for edge in edges:
                self.test_graph1.add_undirected_edge(vertex, edge[0], edge[1])

        self.test_graph2 = Graph()
        self.test_graph2.add_verticies(self.graph2.keys())

        for vertex, edges in self.graph2.items():
            for edge in edges:
                self.test_graph2.add_undirected_edge(vertex, edge[0], edge[1])

        self.test_graph3 = Graph()
        self.test_graph3.add_verticies(self.graph3.keys())

        for vertex, edges in self.graph3.items():
            for edge in edges:
                self.test_graph3.add_undirected_edge(vertex, edge[0], edge[1])

    def test_prims_algorithm_with_graph1(self):
        mst_edges = self.test_graph1.prims_algorithm()
        self.assertEqual(mst_edges, self.expected_output1)

    def test_prims_algorithm_with_graph2(self):
        # YOUR CODE
        mst_edges = self.test_graph2.prims_algorithm()
        self.assertEqual(mst_edges, self.expected_output2)

    def test_prims_algorithm_with_graph3(self):
        ...
        # YOUR CODE
        mst_edges = self.test_graph3.prims_algorithm()
        self.assertEqual(mst_edges, self.expected_output3)


if __name__ == '__main__':
    unittest.main()
