class Solution:
    """
    @param A: an integer array
    @param V: an integer array
    @param m: An integer
    @return: an array
    """
    def backPackIII(self, A, V, m):
        # write your code here
        dp = [0] * (m + 1)
        new_A = []
        for a in A:
            for _ in range(m // a):
                new_A.append(a)
        # 转化为不完全背包
        # 不完全背包解法

        return dp[-1]
