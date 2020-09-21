class Solution:
    """
    @param source : A string
    @param target: A string
    @return: A string denote the minimum window, return "" if there is no such a string
    """
    def minWindow(self, source , target):
        # write your code here
        if not source or not target:
            return ""

        target_to_count = {}
        for char in target:
            target_to_count[char] = target_to_count.get(char, 0) + 1

        char_to_count = {}
        matched = 0
        source_length = len(source)
        target_length = len(target_to_count)
        right = 0
        min_length = float('inf')
        answer = ""
        for left in range(len(source)):
            while right < source_length and matched < target_length:
                char = source[right]
                char_to_count[char] = char_to_count.get(char, 0) + 1
                if char in target_to_count and char_to_count[char] == target_to_count[char]:
                    matched += 1
                right += 1

            if matched == target_length:
                if min_length > right - left:
                    min_length = right - left
                    answer = source[left:right]

            char = source[left]
            char_to_count[char] = char_to_count[char] - 1
            if char in target_to_count and char_to_count[char] < target_to_count[char]:
                matched -= 1

        return answer