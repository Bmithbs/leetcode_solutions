def fourSum(nums, target):
    
    res = []
    left = right = 0
    
    nums.sort()
    length = len(nums)

    # a + b + c + d = target
    # nums[i] = a, nums[j] = b, nums[left] = c, nums[right] = d

    for i in range(length):
        # if nums[i] > target : break # 此句话不应该加，因为 target 有可能是负数
        if i >= 1 and nums[i] == nums[i - 1]: continue
        for j in range(i + 1, length): 
            
            left = j + 1
            right = length - 1

            if j > i + 1 and nums[j] == nums[j - 1]: continue

            while left < right:

                ans = nums[i] + nums[j] + nums[left] + nums[right]

                if ans > target: right -= 1
                elif ans < target: left += 1
                else:
                    res.append([nums[i], nums[j], nums[left], nums[right]])
                    while left != right and nums[left] == nums[left + 1]: left += 1
                    while left != right and nums[right] == nums[right - 1]: right -= 1
                
                    left += 1
                    right -= 1
            
    return res


if __name__ == "__main__":
    nums = [1,0,-1,0,-2,2]
    target = 0
    print(fourSum(nums, target))