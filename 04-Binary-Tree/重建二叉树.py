
class Solution:
    def buildTree(self, preorder, inorder):

        def recur(root, left, right):
            if left > right: return
            node = TreeNode(preorder[root]) # 建立根节点

            i = dic[preorder[root]]
            node.left = recur(root + 1, left, i-1)
            node.right = recur(i-left+root+1, i+1, right)

            return node

        dic, preorder = {}, preorder
        for i in range(len(inorder)):
            dic[inorder[i]] = i
        return recur(0,0,len(inorder) - 1)
