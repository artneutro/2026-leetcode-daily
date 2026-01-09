# https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recursiveCheck(self, root: Optional[TreeNode], level: int) -> Optional[TreeNode]:
        # Case has 2 children
        if root.left != None and root.right != None :
            deep_left = self.recursiveCheck(root.left, level+1)
            deep_right = self.recursiveCheck(root.right, level+1)
            if (deep_left[1] > deep_right[1]) :
                return deep_left
            # Case it reached the leaves
            elif (deep_left[1] == deep_right[1]) :
                # Deepest subtree
                return [root, deep_left[1]]
            else :
                return deep_right
        # Leave
        elif root.left == None and root.right == None :
            return [root, level]
        elif root.left != None and root.right == None :
            return self.recursiveCheck(root.left, level+1)
        elif root.left == None and root.right != None :
            return self.recursiveCheck(root.right, level+1)
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.recursiveCheck(root, 1)[0]
