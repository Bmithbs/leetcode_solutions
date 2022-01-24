def findAnagrams(s, p):

    len_p = len(p)
    len_s = len(s)
    result = []
    
    from collections import Counter

    p_dict = Counter()
    for i in p:
        p_dict[i] += 1

    for i in range(len_s - len_p + 1):
        s_dict = Counter()
        for j in s[i : i + len_p]:
            s_dict[j] += 1

        if s_dict == p_dict:
            result.append(i)

    return result


if __name__ == "__main__":
    s = "abab"
    p = "ab"
    print(findAnagrams(s,p))


'''
注意: 此解法正确，但超出时间限制。
'''

