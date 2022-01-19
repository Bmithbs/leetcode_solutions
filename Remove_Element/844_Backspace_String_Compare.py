def BackspaceCompare(s, t):
    # 本题很自然的想要了用栈来解决，但也可以用双指针来解决

    def build(s):
        ret = list()
        for ch in s:
            if ch != '#':
                ret.append(ch)
            elif ret: # 判断ret中是否为空，如果不为空，则执行出栈操作，不能直接用else语句
                ret.pop()
        return ''.join(ret)

    return build(s) == build(t)