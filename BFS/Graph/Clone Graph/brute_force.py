class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    """
    @param: node: A undirected graph node
    @return: A undirected graph node
    """

    def cloneGraph(self, node):
        # write your code here
        if not node:
            return None
        to_be_copied_list = self.get_nodes(node)

        clone = dict()
        for next_node in to_be_copied_list:
            clone[next_node.label] = UndirectedGraphNode(next_node.label)

        for next_node in to_be_copied_list:
            for neighbor in next_node.neighbors:
                clone[next_node.label].neighbors.append(clone[neighbor.label])

        return clone[node.label]

    def get_nodes(self, node):
        to_be_visited_queue = [node]
        node_list = []
        visited = set()
        while to_be_visited_queue:
            current_node = to_be_visited_queue.pop(0)
            if current_node.label not in visited:
                visited.add(current_node.label)
                node_list.append(current_node)
                for neighbor in current_node.neighbors:
                    to_be_visited_queue.append(neighbor)
        return node_list