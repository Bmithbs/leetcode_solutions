def sortedSquares(nums):
    # 直接进行排序
    return sorted(num ** 2 for num in nums)

if __name__ == '__main__':
    nums = [-4,-1,0,3,10]
    print(sortedSquares(nums))


    
