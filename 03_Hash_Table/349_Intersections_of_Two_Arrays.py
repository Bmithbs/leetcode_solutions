def intersection(nums1, nums2):

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
            if i in n2_dict.keys(): res.append(i)
    else :
        for i in n2_dict.keys():
            if i in n1_dict.keys(): res.append(i)

    return res


    