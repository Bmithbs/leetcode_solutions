class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        if not nums: return 0
        return self.mergeSort(nums, 0, len(nums) - 1)
    def mergeSort(self, nums, l, r):
        if l >= r: return
        mid = (l + r) // 2
        # 递归划分
        cnt = 0
        cnt = self.mergeSort(l, mid) + self.mergeSort(mid + 1, r)
        res = []
        # 合并
        i1, j1 = l, mid
        i2, j2 = mid + 1, r
        idx1, idx2 = i1, i2
        while idx1 <= j1 and idx2 <= j2:
            if nums[idx1] <= nums[idx2]:
                res.append(nums[idx1])
                idx1 += 1
            else:
                res.append(nums[idx2])
                idx2 += 1
                cnt += mid - idx1 + 1
        while idx1 <= j1:
            res.append(nums[idx1])
            idx1 += 1
        while idx2 <= j2:
            res.append(nums[idx2])
            idx2 += 1
            
        nums[l: r + 1] = res
        return cnt