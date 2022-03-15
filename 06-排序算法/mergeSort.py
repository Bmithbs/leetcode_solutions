class solution():  
    def MainMergeSort(self, arr):
        if len(arr) == 0: return 
        result = []
        self.mergeSort(arr, 0, len(arr) - 1, result)

    def mergeSort(self, arr, l, r, result):
        if l >= r: return
        mid = (l + r) // 2
        self.mergeSort(arr, l, mid, result)
        self.mergeSort(arr, mid + 1, r, result)
        self.merge(arr, l, r, result)

    def merge(arr, l, r, result):
        mid = (l + r) //2
        i1, j1 = l, mid
        i2, j2 = mid + 1, r

        idx1, idx2 = i1, i2
        while idx1 <= j1 and idx2 <= j2:
            if arr[idx1] <= arr[idx2]:
                result.append(arr[idx1])
                idx1 += 1
            else:
                result.append(arr[idx2])
                idx2 += 1

        # 将剩余的数字补到结果数组之后
        while idx1 <= j1:
            result.append(arr[idx1])
            idx1 += 1
        while idx2 <= j2:
            result.append(arr[idx2])
            idx2 += 1

        arr[l: r + 1] = result[l : r + 1]





