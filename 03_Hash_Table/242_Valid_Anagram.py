def isAnagram(s, t):

    hash_table = [0] * 26

    for i in s:
        hash_table[ord(i) - ord('a')] += 1

    for i in t:
        hash_table[ord(i) - ord('a')] -= 1
    
    import numpy as np
    return True if sum(np.array(hash_table) ** 2) == 0 else False


if __name__ == '__main__':

    s = 'abc'
    t = 'bac'
    print(isAnagram(s, t))