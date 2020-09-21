import collections

class Solution:
    """
    @param A: the array
    @param K: sum
    @return: the length
    """
    def shortestSubarray(self, A, K):
        # Write your code here.
        if K == 0:
            return 0

        if not A:
            return -1

        cur_sum = 0
        prefix_sums = [0] * (len(A) + 1)
        index = 1
        for a in A:
            cur_sum += a
            prefix_sums[index] = cur_sum
            index += 1

        min_length = float('inf')
        # Maintain a index stack where as the index increases, the prefix sum
        # strictly increases
        stack = collections.deque([])
        for i in range(len(prefix_sums)):
            # When the current index i_1 and first index i_0 in the stack
            # satisfies [i_1:i_0] <= K
            # Record and pop it, test for the next. Repeat until < K to ensure
            # the shortest length is recorded
            # Claim: for any new index i_2, even if [i_2:i_0] satisfies, it
            # will have longer length than [i_1:i_0], so no need to keep index
            # i_0
            while stack and prefix_sums[i] - prefix_sums[stack[0]] >= K:
                min_length = min(min_length, i - stack.popleft())

            # When a smaller prefix i_1 is found, pop i_0 to keep the
            # stack property
            # Claim, no need to keep i_0 because if a new index [i_2:i_0] <= K,
            # then [i_2:i_1] <= K with shorter length. So no need to keep i_0
            # such that i_0 >= i_1
            while stack and prefix_sums[i] <= prefix_sums[stack[-1]]:
                stack.pop()

            stack.append(i)

        return min_length if min_length != float('inf') else -1
