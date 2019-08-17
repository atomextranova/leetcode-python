import pysnooper


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
        to_be_visited_queue = [node]
        clone = {}
        finished = set()
        while to_be_visited_queue:
            current_node = to_be_visited_queue.pop(0)
            if current_node.label not in finished:
                if current_node.label not in clone:
                    clone[current_node.label] = UndirectedGraphNode(current_node.label)
                for neighbor in current_node.neighbors:
                    if neighbor.label not in clone:
                        clone[neighbor.label] = UndirectedGraphNode(neighbor.label)
                    clone[current_node.label].neighbors.append(clone[neighbor.label])
                    finished.add(current_node.label)
                    if neighbor.label not in finished:
                        to_be_visited_queue.append(neighbor)

        return clone[node.label]

node1 = UndirectedGraphNode(1)
node2 = UndirectedGraphNode(2)
node4 = UndirectedGraphNode(4)

node1.neighbors.append(node2)
node1.neighbors.append(node4)
node2.neighbors.append(node1)
node2.neighbors.append(node4)
node4.neighbors.append(node2)
node4.neighbors.append(node1)

sol = Solution()
new_node = sol.cloneGraph(node1)
