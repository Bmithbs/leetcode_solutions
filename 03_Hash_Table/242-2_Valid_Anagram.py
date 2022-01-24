

def isAnagram(s, t):

    
    import collections

    s_dict = collections.Counter()
    t_dict =  collections.Counter()

    for i in s:
        s_dict[i] += 1
    for i in t:
        t_dict[i] += 1

    return s_dict == t_dict


if __name__ == '__main__':

    s = 'abc'
    t = 'bac'
    print(isAnagram(s, t))