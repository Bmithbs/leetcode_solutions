

def getLeastNumbers(arr : list[int], k: int):

    def quick_sort(arr, l, r):

        # 子数组长度为1时终止递归
        if l >= r: return 

        # 哨兵划分操作，以arr[l]作为基准数
        i, j = l, r
        while i < j:
            while i < j and arr[j] >= arr[l]: j -= 1
            while i < j and arr[i] <= arr[l]: i += 1
            arr[i], arr[j] = arr[j], arr[i]
        arr[l], arr[i] = arr[i], arr[l] # 将基数和轴交换

        # 递归左右子数组执行哨兵划分
        quick_sort(arr, l, i - 1)
        quick_sort(arr, i + 1, r)

    quick_sort(arr, 0, len(arr) - 1)
    return arr[:k]



def getLeastNumbers(arr : list[int], k: int):
    def quickSort(arr, l, r):
        if l >= r: return 

        i, j = l, r
        while i < j:
            while i < j and arr[i] <= arr[l]: i += 1
            while i < j and arr[j] >= arr[l]: j -= 1
            arr[i], arr[j] = arr[j], arr[i]

        arr[l], arr[i] = arr[i], arr[l]

        quickSort(arr, l, i - 1)
        quickSort(arr, i + 1, r)
    quickSort(arr, 0, len(arr) - 1)
    return arr[:k]


def getLeastNumbers(arr : list[int], k: int):

    def quick_sort(arr, l, r):
        if l >= r: return 

        i, j = l, r
        while i < j:
            while i < j and arr[i] < arr[l]: i +=1
            while i < j and arr[j] > arr[l]: j -=1
            arr[i], arr[j] = arr[j], arr[i]

        arr[l], arr[i] = arr[i], arr[l]

        quick_sort(arr, l, i - 1)
        quick_sort(arr, i + 1, l)

    quick_sort(arr, 0, len(arr) - 1)
    return arr[:k]

