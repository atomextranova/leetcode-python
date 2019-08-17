class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """

    # Check by choosing each char as the center
    # Time: O(n^2), for n char, each time needs at most n operation to find the longest palindrome
    # A better solution:
    # https://leetcode.com/problems/longest-palindromic-substring/discuss/2923/Simple-C%2B%2B-solution-(8ms-13-lines)
    # Skip duplicate number
    def longestPalindrome(self, s: str) -> str:
        # write your code here
        if not s or s == s[::-1]:
            return s

        longest = 0
        length = 1
        left, right = 0, 0
        for index, my_char in enumerate(s):
            left, right, length = self.find_palindrome(index, index, s, length, left, right)
            left, right, length = self.find_palindrome(index, index + 1, s, length, left, right)

        return s[left:right+1]

    #
    def find_palindrome(self, current_left, current_right, my_str, previous_length, left, right):
        while current_left >= 0 and current_right <= len(my_str) - 1 and my_str[current_left] == my_str[current_right]:
            current_left -= 1
            current_right += 1
        # longest_string = my_str[left+Triangle Count:right]
        # Return only the index and length
        current_length = current_right - current_left - 2 + 1
        if previous_length < current_length:
            return current_left + 1, current_right - 1, current_length
        else:
            return left, right, previous_length


sol = Solution()
print(sol.longest_palindrome_DP("abb"))
