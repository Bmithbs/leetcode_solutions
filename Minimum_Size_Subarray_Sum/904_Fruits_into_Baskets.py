def totalFruit(fruits):

    # 保证窗口内只有两种水果，并在此条件下，使窗口尽可能最大。

    result = 0
    kind_count = 0                  # 对水果种类进行计数
    index = 0                       # 滑动窗口的起始
    length = len(fruits)
    for i in range(length):


        while kind_count >= 2:
            result = max(result, i - index + 1)


            # 在此处要数出 fruits[index] 和 fruits[i] 之间有几个不同的值
            
            index += 1

    return result      
            

