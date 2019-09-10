class Solution:
    def numberToWords(self, num: int) -> str:
        # 0 case
        if num == 0:
            return "Zero"

        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven ' \
               'Twelve ' \
               'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen ' \
               'Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        thousands = ['Thousand', 'Million', 'Billion']
        str_list = []
        self.helper(num, to19, tens, thousands, 0, str_list)
        return " ".join(str_list)

    def helper(self, num, to19, tens, thousands, thousand_index, cur_str):
        larger_part = num // 1000
        rest = num % 1000

        if larger_part > 0:
            # deal with larger part
            self.helper(larger_part, to19, tens, thousands, thousand_index + 1,
                        cur_str)
            # Only append if needed
            # E.g.: 1000000 -> "One Million"
            if larger_part % 1000 > 0:
                cur_str.append(thousands[thousand_index])

        rest %= 1000

        # >= to deal with 100
        if rest >= 100:
            index = rest // 100 - 1
            cur_str.append(to19[index])
            cur_str.append("Hundred")

        rest %= 100

        # >= to deal with 20
        if rest >= 20:
            index = rest // 10 - 2
            cur_str.append(tens[index])
            last_index = rest % 10 - 1
            # Make sure not appending any if last digit is 0
            if last_index >= 0:
                cur_str.append(to19[rest % 10 - 1])

        elif rest > 0:
            # deal with < 20 special case
            cur_str.append(to19[rest - 1])
