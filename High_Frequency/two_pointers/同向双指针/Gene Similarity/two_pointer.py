class Solution:
    """
    @param Gene1: a string
    @param Gene2: a string
    @return: return the similarity of two gene fragments
    """
    def GeneSimilarity(self, Gene1, Gene2):
        # write your code here
        if not Gene1:
            return "0/0"

        total = 0
        matched = 0
        i1 = 0
        i2 = 0
        count_2, char_2, i2 = self.get_count_and_char(i2, Gene2)
        while i1 < len(Gene1):
            count, char, i1 = self.get_count_and_char(i1, Gene1)
            total += count
            # print(count, count_2)
            while count > 0:
                if char == char_2:
                    matched += min(count, count_2)
                if count > count_2:
                    count -= count_2
                    if i2 < len(Gene2):
                        count_2, char_2, i2 = self.get_count_and_char(i2, Gene2)
                elif count == count_2:
                    count = 0
                    count_2 = 0
                else:
                    count_2 -= count
                    count = 0
                # print(count, count_2)

        return str(matched) + "/" + str(total)

    def get_count_and_char(self, start, s):
        count = 0
        while s[start].isdigit():
            count = count * 10 + int(s[start])
            start += 1
        return count, s[start], start + 1

sol = Solution()
print(sol.GeneSimilarity("2T3G", "3T2G"))