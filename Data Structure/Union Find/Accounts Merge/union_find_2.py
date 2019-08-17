import collections


class Solution:
    """
    @param accounts: List[List[str]]
    @return: return a List[List[str]]
    """

    # Union find

    # Time: O(AlogA) where A = sum(len(accounts[i]))
    # Space: O(A)
    def accountsMerge(self, accounts):
        # write your code here

        # email_to_id: mapping each email to i, where i is the index
        # where the email first appears in accounts.
        # Could also map to a unique id. In that case, initialize self.father
        # to the length of all emails that appears in accounts
        # At most(1000 accounts * 10 emails in each account)
        # as specified in the problem
        self.initialize(len(accounts))
        email_to_id = {}

        # Store email to name info
        email_to_name = {}

        for id, account in enumerate(accounts):
            name = account[0]
            emails = account[1:]
            first_email = emails[0]
            for email in emails:
                email_to_name[email] = name
                # only assign new id if the email has not appeared
                if email not in email_to_id:
                    email_to_id[email] = id
                # Union with first email in this account
                self.union(email_to_id[first_email], email_to_id[email])

        ans = collections.defaultdict(list)
        for email in email_to_name.keys():
            ans[self.find(email_to_id[email])].append(email)

        result = []
        for email_list in ans.values():
            name = email_to_name[email_list[0]]
            # Get each merged account [name, email1, email2...]
            temp_result = [name]
            temp_result.extend(sorted(email_list))
            result.append(temp_result)
        return result

    def initialize(self, length):
        self.father = {}
        for i in range(length):
            self.father[i] = i

    # path compression
    # O(n) first, afterwards O(log*n), almost O(1)
    def find(self, id):
        if self.father[id] != id:
            self.father[id] = self.find(self.father[id])
        return self.father[id]

    # O(1) given find is O(1)
    def union(self, id_1, id_2):
        root_1 = self.find(id_1)
        root_2 = self.find(id_2)
        if root_1 != root_2:
            self.father[root_1] = root_2
