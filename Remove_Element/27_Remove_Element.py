def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """


    # 利用双指针法，将两个for循环变为一个
    # 时间复杂度 O(n)
    # 空间复杂度 O(1)

    fast = slow = 0
    while fast < len(nums):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1

        # 当 fast 指针遇到要删除的元素时停止赋值
        # slow 指针停止移动, fast 指针继续前进
    return slow

    



if __name__ == '__main__':
    nums = [3,2,2,3]
    val = 3
    length = removeElement(nums, val)
    print(length)
    print(nums)



