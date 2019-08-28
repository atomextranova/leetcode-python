from collections import deque


class Solution:
    """
    @param deadends: the list of deadends
    @param target: the value of the wheels that will unlock the lock
    @return: the minimum total number of turns
    """

    # Edge case
    # 1. not target
    # 2. target = "0000" (start = end)
    # 3. start in deadends
    def openLock(self, deadends, target):
        # Write your code here
        if not target:
            return -1

        if target == "0000":
            return 0

        if "0000" in deadends:
            return -1

        self.start_queue = deque(["0000"])
        self.end_queue = deque([target])

        self.start_length = {}
        self.end_length = {}

        self.start_length["0000"] = 0
        self.end_length[target] = 0

        while self.start_queue and self.end_queue:
            start_word = self.start_queue.popleft()
            next_word_list = self.generate_next_words(start_word)
            for next_word in next_word_list:
                if next_word in self.start_length:
                    continue
                if next_word in deadends:
                    continue
                if next_word in self.end_length:
                    return self.start_length[start_word] + \
                           self.end_length[next_word] + 1
                self.start_length[next_word] = self.start_length[start_word] + 1
                self.start_queue.append(next_word)

            end_word = self.end_queue.popleft()
            next_word_list = self.generate_next_words(end_word)
            for next_word in next_word_list:
                if next_word in self.end_length:
                    continue
                if next_word in deadends:
                    continue
                if next_word in self.start_length:
                    return self.start_length[next_word] + \
                           self.end_length[end_word] + 1
                self.end_length[next_word] = self.end_length[end_word] + 1
                self.end_queue.append(next_word)

        return -1

    def generate_next_words(self, word):
        word_list = []
        for i, char in enumerate(word):
            for dx in (-1, 1):
                new_char_val = int(char) + dx
                if new_char_val == -1:
                    new_char_val = 9
                if new_char_val == 10:
                    new_char_val = 0

                new_word = word[:i] + str(new_char_val) + word[i + 1:]
                word_list.append(new_word)

        return word_list


sol = Solution()
sol.openLock(["2110","2000","0000","2111","1110"]
, "0012")