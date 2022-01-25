def fourSumCount(nums1, nums2, nums3, nums4):
    import collections
    hashmap = collections.Counter()

    for i in nums1:
        for j in nums2:
            if i + j in hashmap:
                hashmap[i + j] += 1
            else:
                hashmap[i + j] = 1

    cnt = 0
    for i in nums3:
        for j in nums4:
            key = - i - j
            if key in hashmap:
                cnt += hashmap[key]

    return cnt 

    # 领悟这种思想

if __name__ == '__main__':
    nums1 = [1,2]
    nums2 = [-2,-1]
    nums3 = [-1,2]
    nums4 = [0,2]

    print(fourSumCount(nums1, nums2, nums3, nums4))
