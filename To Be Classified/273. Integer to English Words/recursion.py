class Solution:
    def numberToWords(self, num: int) -> str:
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
               'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        thousand = 'Thousand Million Billion'.split()
        result_list = self.word(num, to19, tens, thousand, 0)
        if not result_list:
            return "Zero"
        return " ".join(result_list)

    def word(self, num, to19, tens, thousand, index_thousand): \
            # Deal with 0
        if num == 0:
            return []
        # Deal with 2 digit case
        elif num < 20:
            return [to19[num - 1]]
        elif num < 100:
            return [tens[num // 10 - 2]] + self.word(num % 10, to19, tens,
                                                     thousand, index_thousand)
        # Deal with 3 digit case
        elif num < 1000:
            return [to19[num // 100 - 1]] + ["Hundred"] + self.word(num % 100,
                                                                    to19, tens,
                                                                    thousand,
                                                                    index_thousand)

        left_part, right_part = num // 1000, num % 1000
        if left_part % 1000 > 0:
            return self.word(left_part, to19, tens, thousand,
                             index_thousand + 1) + [thousand[index_thousand]] + \
                   self.word(right_part, to19, tens, thousand,
                             index_thousand + 1)
        else:
            return self.word(left_part, to19, tens, thousand,
                             index_thousand + 1) + \
                   self.word(right_part, to19, tens, thousand,
                             index_thousand + 1)
