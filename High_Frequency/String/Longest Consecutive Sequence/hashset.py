class Solution:
    """
    @param num: A list of integers
    @return: An integer
    """

    # Edge case
    # Duplicates?
    # Empty num

    def longestConsecutive(self, num):
        # write your code here
        if not num:
            return 0

        num_dict = set()
        for n in num:
            num_dict.add(n)

        longest = 0

        for n in num:
            if n not in num_dict:
                continue

            cur_length = 1
            num_dict.remove(n)
            l_value = n - 1
            r_value = n + 1
            while l_value in num_dict:
                cur_length += 1
                num_dict.remove(l_value)
                l_value -= 1

            while r_value in num_dict:
                cur_length += 1
                num_dict.remove(r_value)
                r_value += 1

            longest = max(longest, cur_length)

        return longest

