import sys
import unittest
from graph import Graph
from dijkstra import dijkstra


class TestDijkstraAlgorithm(unittest.TestCase):
    def setUp(self):
        self.graph = Graph(9)
        self.graph.add_edge(0, 1, 4)
        self.graph.add_edge(0, 7, 8)
        self.graph.add_edge(1, 7, 5)
        self.graph.add_edge(1, 2, 8)
        self.graph.add_edge(2, 3, 7)
        self.graph.add_edge(2, 5, 8)
        self.graph.add_edge(3, 4, 10)
        self.graph.add_edge(3, 5, 12)
        self.graph.add_edge(5, 4, 10)
        self.graph.add_edge(6, 5, 4)
        self.graph.add_edge(6, 8, 1)
        self.graph.add_edge(7, 6, 5)
        self.graph.add_edge(7, 8, 7)
        self.graph.add_edge(8, 2, 3)

    def test_dijkstra_for_source_root_0(self):
        result = dijkstra(self.graph, 0)
        self.assertEqual(result, [0, 4, 12, 19, 27, 17, 13, 8, 14])

    def test_dijkstra_for_source_root_1(self):
        result = dijkstra(self.graph, 1)
        self.assertEqual(result, [sys.maxsize, 0, 8, 15, 24, 14, 10, 5, 11])

    def test_dijkstra_for_source_root_5(self):
        result = dijkstra(self.graph, 5)
        self.assertEqual(result, [sys.maxsize, sys.maxsize, sys.maxsize,
                                  sys.maxsize, 10, 0, sys.maxsize,
                                  sys.maxsize, sys.maxsize])

    def test_dijkstra_for_unreachable_source_4(self):
        result = dijkstra(self.graph, 4)
        expected_result = [sys.maxsize] * 9
        expected_result[4] = 0
        self.assertEqual(result, expected_result)

    def test_invalid_source_vertex(self):
        with self.assertRaises(ValueError):
            dijkstra(self.graph, 9)

    def test_invalid_source_vertex_negative(self):
        with self.assertRaises(ValueError):
            dijkstra(self.graph, -1)

    def test_single_vertex_graph(self):
        graph = Graph(1)
        result = dijkstra(graph, 0)
        self.assertEqual(result, [0])


if __name__ == '__main__':
    unittest.main()
