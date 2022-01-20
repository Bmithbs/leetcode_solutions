def sortedSquares(nums):
    # 利用双指针法

    left_pointer = 0
    length = len(nums)
    right_pointer = length - 1
    new_list = [0] * length
    new_list_ponter = right_pointer # 因为题目要求升序，因此从新数组的最后一位开始填充元素
    while left_pointer <= right_pointer:

        if nums[left_pointer] ** 2 > nums[right_pointer] ** 2:
            new_list[new_list_ponter] = nums[left_pointer] ** 2
            left_pointer += 1
        else :
            new_list[new_list_ponter] = nums[right_pointer] ** 2
            right_pointer -= 1
        
        new_list_ponter -= 1
    
    return new_list


if __name__ == '__main__':
    nums = [-4,-1,0,3,10]
    print(sortedSquares(nums))


    
