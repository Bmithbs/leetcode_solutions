def minSubArrayLen(target, nums):
    # 滑动窗口法

    # 题目要求返回最小子串的长度
    result = float("inf")                           # 定义一个无限大的数
    sum = 0
    index = 0                                       # 表示滑动窗口的起始位置
    for i in range(len(nums)):
        sum += nums[i]


        # 此处使用 while 每次更新 index (起始位置)，并不断比较子列是否符合条件
        while sum >= target:
            result = min(result, i - index + 1)     # i - index + 1 表示滑动窗口的长度
            sum -= nums[index]
            index += 1                              # 这里体现出滑动窗口的精髓之处，不断变更子列的起始位置 index 
    
    return 0 if result == float("inf") else result


