# 利用双指针的方法进行

def threeSum(nums):
    nums.sort()     # 首先要对nums进行排序，然后利用双指针法
    res = []        # 结果存在这里
    left ,right = 0, 0 
    length = len(nums)

    # 找出 a + b + c = 0
    # a = nums[i], b = nums[left], c = nums[right]
     
    for i in range(length): 
        left  = i + 1
        right = length - 1

        # 排序之后如果第一个元素已经大于0，那么无论如何也不能凑成符合条件的数组， 因此直接返回空
        if nums[i] > 0: break  
        # 去重方法，去掉重复的 i，保证返回的每个数组是不同的
        if i >= 1 and nums[i] == nums[i - 1]:
            continue

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total > 0: right -= 1    # 如果三数和大于 0，则右指针左移
            elif total < 0: left += 1   # 如果三数和小于0， 则左指针右移
            else:
                res.append([nums[i], nums[left], nums[right]])
                while left != right and nums[left] == nums[left + 1] : left += 1    # 跳过重复的
                while left != right and nums[right] == nums[right - 1] : right -= 1 # 跳过重复的
                left  += 1
                right -= 1
    return res
