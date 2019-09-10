class Solution:
    # Edge case:
    # [] x False
    # [0] x False, only sum is considered
    # [0, 0] x True
    # [x, x] 0 False if x != 0
    # [1, 0] 2 False

    # 检查空数组
    # 初始化，dict加入0,-1,key为余数，value为index
    # 对每个数，如果k！=0,取余数
    # 如果相同余数不存在，设为当前index
    # 否则，检查上一个相同余数距离>=2 (所以difference至少为2或者更多数之和)
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if not nums:
            return False

        remainder_to_index = {}
        remainder_to_index[0] = -1
        remaining = 0
        for i in range(0, len(nums)):
            num = nums[i]
            remaining += num
            if k != 0:
                remaining = remaining % k
            if remaining in remainder_to_index:
                if i - remainder_to_index[remaining] > 1:
                    return True
            else:
                remainder_to_index[remaining] = i

        return False