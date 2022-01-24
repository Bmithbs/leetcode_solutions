def findAnagrams(s, p):

    len_p = len(p)
    len_s = len(s)
    result = []
    if len_s < len_p: return result
    
    p_cnt = [0] * 26
    s_cnt = [0] * 26


    for i in range(len_p):
        p_cnt[ord(p[i]) - ord('a')] += 1
        s_cnt[ord(s[i]) - ord('a')] += 1

    if p_cnt == s_cnt: result.append(0)


    for i in range(len_p,len_s):

        # 有些类似滑动窗口的思想
        s_cnt[ord(s[i - len_p]) - ord('a')] -= 1 # 一个元素一个元素的进行判断
        s_cnt[ord(s[i]) - ord('a')] += 1 
        if s_cnt == p_cnt:
            result.append(i - len_p + 1)

    return result


if __name__ == "__main__":
    s = "abab"
    p = "ab"
    print(findAnagrams(s,p))


'''
注意: 此解法正确，但超出时间限制。
'''

