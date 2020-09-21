def find_first_number(self, nums, target):
    left = 0 # 下界
    right = len(nums) - 1 # 上界

    while left + 1 < right:
    # 用//防止出现小数
        mid = (left + right) // 2


    if nums[mid] < target:
        left = mid
    elif nums[mid] > target:
        right = mid
    else:
        right = mid

    if nums[left] == target:
        return left

    if nums[right] == target:
        return right