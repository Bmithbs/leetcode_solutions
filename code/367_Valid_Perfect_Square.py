def isPerfectSquare(self, num):
    """
    :type num: int
    :rtype: bool
    """

    def MySqrt(num):
        left, right = 0, num
        while left <= right:
            mid = (left + right) // 2
            if mid ** 2 > num:
                right = mid - 1
            elif mid ** 2 < num:
                left = mid + 1
            else :
                return mid
        return left - 1 

    if MySqrt(num) ** 2 == num : return True
    else: return False