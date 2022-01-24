
def intersect(nums1, nums2):
    from collections import Counter

    n1_dict = Counter()
    n2_dict = Counter()
    res = []

    for i in nums1:
        n1_dict[i] += 1
    for i in nums2:
        n2_dict[i] += 1

    if len(nums1) <= len(nums2):
        for i in n1_dict.keys():
            if i in n2_dict.keys(): 
                times = min(n1_dict[i], n2_dict[i])
                for _ in range(times):
                    res.append(i)
    else :
        for i in n2_dict.keys():
            if i in n1_dict.keys():
                times = min(n1_dict[i], n2_dict[i])
                for _ in range(times):
                    res.append(i)

    return res


if __name__ == '__main__':
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    print(intersect(nums1, nums2))
