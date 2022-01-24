import enum


def twoSum(nums, target):

    record = dict()
    for idx, i in enumerate(nums):
        if target - i not in record:
            record[i] = idx
        else:
            return [record[target - i], idx] 