class Solution:
    """
    @param n: an integer, denote the number of courses
    @param p: a list of prerequisite pairs
    @return: return an integer,denote the number of topologicalsort
    """
    def topologicalSortNumber(self, n, p):
        post_to_pres = []
        cur_list = [str(i) for i in range(n)]
        memo = {}

        for i in range(n):
            post_to_pres.append(set())
        for (pre, post) in p:
            post_to_pres[post].add(pre)

        # return self.dfs(post_to_pres, post_to_count, cur_list, memo)
        result = self.dfs(post_to_pres, cur_list, memo)
        return result

    def dfs(self, post_to_pres, cur_list, memo):
        if len(cur_list) == 0:
            return 1

        key = "".join(cur_list)
        if key in memo:
            return memo[key]

        memo[key] = 0
        for i in range(len(cur_list)):
            cur_course = int(cur_list[i])
            if len(post_to_pres[cur_course]) != 0:
                continue
            next_list = cur_list[:i] + cur_list[i+1:]
            remove_list = []
            for course in next_list:
                course = int(course)
                if cur_course in post_to_pres[course]:
                    post_to_pres[course].remove(cur_course)
                    remove_list.append(course)
            memo[key] += self.dfs(post_to_pres, next_list, memo)
            for course in remove_list:
                post_to_pres[course].add(cur_course)

        return memo[key]