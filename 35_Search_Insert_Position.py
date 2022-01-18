def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    
    length = len(nums)
    left = 0
    right = length - 1
    while left <= right:
        mid = (right + left) // 2
        if target > nums[mid]: left = mid + 1
        elif target < nums[mid]: right = mid - 1
        else: return mid 

    return left

if __name__ == "__main__":
    nums = [1,3,5,6]
    target = 2
    x = searchInsert(nums, target)
    print(x)  