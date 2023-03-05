# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # TC: O(n) n = number of nodes, because we are traversing through 
    # each node once.

    # SC: O(n), n = number of nodes
    # If the height is not properly balanced, in the worst case the height
    # will be n, but if it's a properly balanced binary tree, the height 
    # will be O(logn).
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        return max(left_height, right_height) + 1
