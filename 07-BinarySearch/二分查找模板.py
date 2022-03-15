def binarySearch1(nums, target):
    if not nums: return -1

    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
        else:
            return mid
    # End Condition: left > right
    return -1
'''
关键属性：
1. 二分查找的最基础和最基本的形式
2. 不需要后处理，因为每一步中，都在检查是否找到了元素，如果到达末尾，则知道未找到该元素
'''