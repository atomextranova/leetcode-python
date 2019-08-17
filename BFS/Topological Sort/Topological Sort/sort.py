"""
Definition for a Directed graph node
"""
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []



class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """

    def topSort(self, graph):
        # write your code here
        if not graph:
            return []

        in_degree = {node.label: 0 for node in graph}
        for next_node in graph:
            for neighbor in next_node.neighbors:
                in_degree[neighbor.label] += 1
        to_be_sorted = []
        result = []

        for node in graph:
            if in_degree[node.label] == 0:
                to_be_sorted.append(node)
                result.append(node)

        while to_be_sorted:
            node = to_be_sorted.pop(0)
            for neighbor in node.neighbors:
                in_degree[neighbor.label] -= 1
                if in_degree[neighbor.label] == 0:
                    to_be_sorted.append(neighbor)
                    result.append(neighbor)

        return result