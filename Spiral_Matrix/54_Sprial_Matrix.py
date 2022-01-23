import numpy


def spiralOrder(matrix):

    # Description:
    # Given an m x n matrix, return all elements of the matrix in spiral order.

    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """


    new_matrix = []
    if not matrix: return new_matrix
    hight, width = numpy.shape(matrix)
    

    left ,right, top, bottom = 0, width - 1, 0, hight - 1

    while True:

        for i in range(left, right + 1):
            new_matrix.append(matrix[top][i])
            
        top += 1
        if top > bottom: break

        for i in range(top, bottom + 1):
            new_matrix.append(matrix[i][right])

        right -= 1
        if right < left: break

        for i in range(right, left - 1, -1):
            new_matrix.append(matrix[bottom][i])

        bottom -= 1
        if bottom < top: break

        for i in range(bottom , top - 1, -1):
            new_matrix.append(matrix[i][left])

        left += 1
        if left > right: break
        

    # if hight == width and hight % 2 :
    #     new_matrix.append(matrix[width // 2][hight // 2]) 
    
    # if hight % 2 and width % 2 and hight != width: # 如果宽高都为奇数，且宽高不同
    #     new_matrix = new_matrix[:-1]

    
    return new_matrix

if __name__ == '__main__':
    matrix =[[1,2,3,4],[5,6,7,8],[9,10,11,12]]

    print(spiralOrder(matrix))



        

        



