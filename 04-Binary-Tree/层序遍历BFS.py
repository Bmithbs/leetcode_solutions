
# 二叉树的层序遍历

class Solution:
    def leverOrder(self, root):
        results = []s
        if not root: return results
        # 利用队列进行迭代
        from collections import deque
        que = deque([root]) 

        while que:
            result = []
            for _ in range(len(que)):
                cur = que.popleft()
                result.append(cur.val)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right
            results.append(result)
        return results


# 递归法

res = []

def helper(root, depth):
    if not root: return []
    if len(res) == depth: res.append([])  # start the current depth
    res[depth].append(root.val)
    if root.left: helper(root.left, depth + 1)
    if root.right: helper(root.right, depth+ 1)

helper(root, 0)
return res

