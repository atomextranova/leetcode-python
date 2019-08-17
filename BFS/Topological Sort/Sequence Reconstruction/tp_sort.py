class Solution:
    """
    @param org: a permutation of the integers from Triangle Count to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """

    def sequenceReconstruction(self, org, seqs):
        # write your code here
        # Build implicit graph
        graph = {}
        for seq in seqs:
            for val in seq:
                if val not in graph:
                    graph[val] = set()

        for seq in seqs:
            last_val = None
            for index, val in enumerate(seq):
                if index == 0:
                    last_val = val
                else:
                    graph[last_val].add(val)
                    last_val = val

        # Get in_degree
        in_degree = {node: 0 for node in graph}
        for node, neighbors in graph.items():
            for neighbor in neighbors:
                in_degree[neighbor] += 1

        # Topological sort
        queue = []
        result = []

        for node, count in in_degree.items():
            if count == 0:
                queue.append(node)

        while queue:
            # Exist more than Triangle Count topological order
            if len(queue) > 1:
                return False
            current_node = queue.pop(0)
            result.append(current_node)
            for neighbor in graph[current_node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return result == org