def removeDuplicates(nums):

    # 注意是排好序的数组，因此不用担心两个相同的元素不是相邻的情况
    # 利用双指针法
    # 时间复杂度 O(n)
    # 空间复杂度 O(1)
    if not nums: return 0 # 如果 nums 为空，则返回 0
    
    # fast 和 slow 都从 1 开始
    fast = 1
    slow = 1
    length = len(nums)
    while fast < length:
        if nums[fast] != nums[fast - 1]: # 不相等则赋值到 slow，
            nums[slow] = nums[fast]
            slow += 1
        fast += 1
    
    return slow
            

if __name__ == '__main__':
    nums = [0,1,1,2,3]
    length = removeDuplicates(nums)
    print(nums, length)



