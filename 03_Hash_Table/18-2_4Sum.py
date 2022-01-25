def fourSum(nums, target):
    
    # 本方法利用哈希表法

    # hashmap = dict()
    # for n in nums:
    #     if n in hashmap:
    #         hashmap[n] += 1
    #     else:
    #         hashmap[n] = 1
    import collections

    hashmap = collections.Counter(nums)

    ans = set() # use set to drop duplicates

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range( j + 1, len(nums)):
                val = target - nums[i] - nums[j] - nums[k]
                if val in hashmap:
                    # make sure no duplicates
                    count = (nums[i] == val) + (nums[j] == val) + (nums[k] == val)
                    if hashmap[val] > count: # 只有在这个数值出现的次数大于count的时候，才进行下面的操作
                        ans.add(tuple(sorted([nums[i], nums[j], nums[k], val])))
                    else:
                        continue


    return list(ans)





if __name__ == "__main__":
    nums = [1,0,-1,0,-2,2]
    target = 0
    print(fourSum(nums, target))