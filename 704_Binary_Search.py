
def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    length = len(nums)
    left = 0
    right = length - 1
    while left < right:
        mid = (left + right) // 2
        if target > nums[mid]:
            left = mid + 1
        elif target < nums[mid]:
            right = mid - 1
        else:
            return mid

    if nums[left] == nums[right] == target: return left
    else: return -1

if __name__ == "__main__":
    nums = [-1,0,3,5,9,12]
    target = 9
    x = search(nums, target)
    print(x)

       

