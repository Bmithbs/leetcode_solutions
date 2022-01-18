# 参考资料：https://programmercarl.com/0034.在排序数组中查找元素的第一个和最后一个位置.html



def searchRange(nums, target):
    # if len(nums) == 0: return [-1, -1]
    # if len(nums) == 1 and nums[0] == target:
    #     return [0, 0]
    # else: 
    #     return [-1, -1]
    def BinarySearch(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target: 
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1
    
    # if nums[mid] != target: return [-1, -1]
    index = BinarySearch(nums, target)
    if index == -1: return [-1, -1]

    left = right = index

    
    for i in range(index):
        if nums[i] == target:
            left = i
            break
    while right + 1 < len(nums) and nums[right + 1] == target: right += 1
    
    return [left, right]

if __name__ == "__main__":
    nums = [0,2]
    target = 2
    x = searchRange(nums, target)
    print(x)