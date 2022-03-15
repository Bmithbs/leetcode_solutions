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

def Sqrt(x, precision):
    flag = 1
    if x < 0: 
        x = -x
        flag = -1
    l, r = 0, x
    while l < r:
        mid = (l + r) / 2
        if abs(mid ** 3 - x) < precision:
            return mid * flag
        elif mid ** 3 > x:
            r = mid
        elif mid ** 3 < x:
            l = mid 

if __name__ == '__main__':
    
    y = Sqrt(-56, 0.01)
    print(y)
    

