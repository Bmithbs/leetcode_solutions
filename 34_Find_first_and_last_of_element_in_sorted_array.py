# 参考资料：https://programmercarl.com/0034.在排序数组中查找元素的第一个和最后一个位置.html

def searchRange(nums, target):

    def GetLeftBorder(nums, target):
        left, right = 0, len(nums) - 1
        left_border = -2
        while left <= right:
            mid = left + (right - left) // 2 # 防止溢出
            if nums[mid] >= target: # 此处的 = 是关键
                right = mid - 1
                left_border = right
            else:
                left = mid + 1
        return left_border

    def GetRightBorder(nums, target):
        left, right = 0, len(nums) - 1
        right_border = -2
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
                right_border = left
        return right_border

    left_border = GetLeftBorder(nums, target)
    right_border = GetRightBorder(nums, target)

    if left_border == -2 or right_border == -2: return [-1, -1]
    if right_border - left_border > 1: return [left_border + 1, right_border - 1]
    return [-1, -1]

