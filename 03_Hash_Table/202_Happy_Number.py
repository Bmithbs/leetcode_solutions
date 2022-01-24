def isHappy(n):

    def getHappy(n):
        sum = 0
        while n:
            sum += (n % 10) ** 2
            n = n // 10
        return sum

    record = set()
    while True:

        n = getHappy(n)
        if n == 1: return True

        if n in record:
            return False
        else :
            record.add(n)


if __name__ == '__main__':
    n = 19
    print(isHappy(n))

     

