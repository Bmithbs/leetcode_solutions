def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """

    left, right = 0, x
    while left <= right:
        mid = (left + right) // 2
        if mid ** 2 > x:
            right = mid - 1
        elif mid ** 2 < x:
            left = mid + 1
        else :
            return mid
        
    
    return left - 1

if __name__ == '__main__':
    for i in range(0, 100):
        y = mySqrt(i)
        print(i, y)

