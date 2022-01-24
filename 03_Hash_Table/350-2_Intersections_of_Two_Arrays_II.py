
def intersect(nums1, nums2):
    from collections import Counter

    n1_dict = Counter(nums1)
    n2_dict = Counter(nums2)
    num = n1_dict & n2_dict
    res = list(num.elements())
    return res


if __name__ == '__main__':
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    print(intersect(nums1, nums2))
