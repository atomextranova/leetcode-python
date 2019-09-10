operators = ["+", "-", "*"]


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        result = []
        for i in range(1, len(num) + 1):
            # Avoid "0**"
            if i == 1 or (i > 1 and num[0] != "0"):
                temp_operand = num[:i]
                temp_val = int(temp_operand)
                self.dfs_helper(num, target, len(num), i, result, temp_operand,
                                temp_val, temp_val)
        return result

    def dfs_helper(self, num, target, length, index, result, temp_operand,
                   prev_val_change, prev_val):

        if index == length:

            if prev_val == target:
                result.append(temp_operand)
            return

        for i in range(index + 1, length + 1):
            # index is the start index to insert operand
            # i stands for next char not included in current
            # expression
            # Avoid "0**"
            if i == index + 1 or (i > index + 1 and num[index] != "0"):
                cur_operand = num[index:i]
                cur_val = int(cur_operand)
                self.dfs_helper(num, target, length, i, result,
                                temp_operand + "+" + cur_operand, cur_val,
                                cur_val + prev_val)
                self.dfs_helper(num, target, length, i, result,
                                temp_operand + "-" + cur_operand, -cur_val,
                                prev_val - cur_val)
                # Key: revert back prev_val_change to correctly
                # handle * case. Only * prev_val_change
                # Ex1:
                # 4 * 2 - 3 * 10, revert 3:
                # 4*2 - 3 = 5
                # (5 - (-3)) + (-3) * 10
                # Ex2:
                # 4 * 2 - 3 *2 * 10
                # first revert change by -3, add -3*2
                # then revert change by -3 * 2, add -3*2*10
                # where -3*2 is prev_val_change
                orig_val = prev_val - prev_val_change
                val_change = prev_val_change * cur_val
                next_val = orig_val + val_change
                self.dfs_helper(num, target, length, i, result,
                                temp_operand + "*" + cur_operand, val_change,
                                next_val)