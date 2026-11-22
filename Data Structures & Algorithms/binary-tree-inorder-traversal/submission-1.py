# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recur(self,node,ans):
        if not node:
            return
        self.recur(node.left,ans)
        ans.append(node.val)
        self.recur(node.right,ans)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.recur(root,ans)
        return ans