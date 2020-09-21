import collections

class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        # write your code here
        visited = set()
        deque = collections.deque([start])
        visited.add(start)
        distance = 1
        while deque:
            for _ in range(len(deque)):
                word = deque.popleft()
                for i in range(len(word)):
                    for char in "abcdefghijklmnopqrstuvwxyz":
                        next_word = word[:i] + char + word[i+1:]
                        if next_word == end:
                            return distance + 1
                        if next_word in dict and next_word not in visited:
                            deque.append(next_word)
                            visited.add(next_word)
            distance += 1

        return 0

sol = Solution()
print(sol.ladderLength(
    "red",
    "tax",
    ["ted","tex","red","tax","tad","den","rex","pee"]))
