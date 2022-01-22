def MyMinSubArrayLength(target, nums):

    result = len(nums) + 1
    index = 0
    sum = 0 
    for i in range(len(nums)):
        sum += nums[i]

        while sum >= target:
            result = min(result, i - index + 1)
            sum -= nums[index]
            index += 1

    return 0 if result == len(nums) + 1 else result 

