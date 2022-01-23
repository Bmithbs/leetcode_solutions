import collections


def totalFruit(fruits):

    # 保证窗口内只有两种水果，并在此条件下，使窗口尽可能最大。

    ans = 0 # ans 表示水最终水果的最大数量
    i = 0 # 表示滑动窗的起始位置
    count = collections.Counter() # 定义 count，count是一个字典类型
    for j, x in enumerate(fruits):
        count[x] += 1     # x 为字典的健， 对其值加 1
        while len(count) >= 3: # 如果 count 有三个及三个以上的健的话，进入 while 循环，调整窗口的起始位置，并调整 count 中的键值
            count[fruits[i]] -= 1 
            if count[fruits[i]] == 0: del count[fruits[i]] # 删除滑动窗口起始的键

            i += 1 # 滑动窗口的起始位置加一
        ans = max(ans, j - i + 1) # 返回 ans 值

    return ans


if __name__ == '__main__':
    fruits = [1,2,3,2,2]
    print(totalFruit(fruits))

            

