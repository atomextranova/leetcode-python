class Solution:
    # Could use memo if m is large, or n - m is large,
    # or if need to print every road
    def numberOfPatterns(self, m: int, n: int) -> int:
        memo = [[set()] * (n - m + 1) for _ in range(10)]
        skip = [[0 for j in range(10)] for i in range(10)]
        skip[1][3] = skip[3][1] = 2
        skip[1][7] = skip[7][1] = 4
        skip[3][9] = skip[9][3] = 6
        skip[7][9] = skip[9][7] = 8
        skip[1][9] = skip[9][1] = skip[2][8] = skip[8][2] = skip[3][7] = \
        skip[7][3] = skip[4][6] = skip[6][4] = 5
        visited = [False] * 10
        # 1,3,7,9 are symmetric
        # 2,4,6,8 are symmetric
        # 5 is special

        result = 0
        for i in range(m, n + 1):
            result += self.dfs(1, skip, 1, i, visited) * 4
            # print(result)
            result += self.dfs(2, skip, 1, i, visited) * 4
            # print(result)
            result += self.dfs(5, skip, 1, i, visited)
            # print(result)

        return result

    # Continue dfs if next_key not yet visited and the num between
    # cur_key and next_key is visited or does not exist
    def dfs(self, cur_key, skip, current_length, max_length, visited):
        if current_length == max_length:
            return 1
        visited[cur_key] = True
        result = 0
        for next_key in range(1, 10):
            if visited[next_key]:
                continue

            skip_num = skip[cur_key][next_key]
            if skip_num == 0 or visited[skip_num]:
                result += self.dfs(next_key, skip, current_length + 1, max_length,
                                   visited)

        visited[cur_key] = False

        return result

