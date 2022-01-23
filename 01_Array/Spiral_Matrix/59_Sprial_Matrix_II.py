def generateMatrix(n):

    matrix = [[0] * n for _ in range(n)]

    left, right, top, bottom = 0, n - 1, 0, n - 1
    number = 1

    while left < right and top < bottom:

        for i in range (left, right):
            matrix[top][i] = number
            number += 1

        for i in range(top, bottom):
            matrix[i][right] = number
            number += 1
        
        for i in range(right, left, -1):
            matrix[bottom][i] = number
            number += 1

        for i in range (bottom, top, -1):
            matrix[i][left] = number
            number += 1

        left += 1
        right -= 1
        top -= 1
        bottom += 1

    if n % 2:
        matrix[n//2][n//2] = number

    return matrix
