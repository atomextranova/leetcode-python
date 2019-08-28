
class LoadBalancer:
    def __init__(self):
        # do intialization if necessary
        self.server_list = []
        self.server_to_index = {}

    """
    @param: server_id: add a new server to the cluster
    @return: nothing
    """

    def add(self, server_id):
        # write your code here
        # Look up in {} >> look up in list
        if server_id in self.server_to_index:
            return
        index = len(self.server_list)
        self.server_to_index[server_id] = index
        self.server_list.append(server_id)

    """
    @param: server_id: server_id remove a bad server from the cluster
    @return: nothing
    """

    def remove(self, server_id):
        # write your code here
        if server_id not in self.server_to_index:
            return
        index = self.server_to_index[server_id]
        del self.server_to_index[server_id]
        last_server = self.server_list[-1]
        self.server_list[index] = last_server
        self.server_to_index[last_server] = index

        self.server_list.pop()

    """
    @return: pick a server in the cluster randomly with equal probability
    """

    def pick(self):
        import random
        # write your code here
        index = random.randint(0, len(self.server_list) - 1)
        return self.server_list[index]