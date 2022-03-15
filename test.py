
def findMedianSortedArrays(nums1, nums2) :

    res = []

    l1 = 0
    l2 = 0
    while l1 <= len(nums1) - 1 and l2 <= len(nums2) - 1:
        if l1 == len(nums1) - 1:
            res.append(nums2[l2])
            l2 += 1
        elif l2 == len(nums2) - 1:
            res.append(nums1[l1])
            l1 += 1
        elif nums1[l1] <= nums2[l2]:
            res.append(nums1[l1])
            l1 += 1
        else:
            res.append(nums2[l2])
            l2 += 1



    if len(res) % 2 == 1: return res[len(res) // 2]
    else: return (res[len(res)//2 -1] + res[len(res)//2])/2

l1 = [1,3]
l2 = [2]
print(findMedianSortedArrays(l1,l2))