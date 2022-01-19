def removeDuplicates(nums):

    # 注意是排好序的数组，因此不用担心两个相同的元素不是相邻的情况
    # 利用双指针法
    # 时间复杂度 O(n)
    # 空间复杂度 O(1)
    
    fast = 1
    slow = 0
    length = len(nums)
    while fast < length:
        if nums[fast] != nums[slow]:
            if (fast - slow) > 1:  # 优化，不用每次赋值
                nums[slow + 1] = nums[fast]
            slow += 1
        fast += 1
    
    return slow + 1 
            

if __name__ == '__main__':
    nums = [0,1,1,2,3]
    length = removeDuplicates(nums)
    print(nums, length)



