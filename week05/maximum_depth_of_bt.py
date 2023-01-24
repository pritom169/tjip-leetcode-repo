class Solution:
    # TC: O(N), N = Number of nodes. 
    # We are traversing thourgh each node once.

    # SC: O(N), N = number of nodes
    # The height of the binary tree will be logN if the
    # height is balanced. However, in the worst case, if
    # the tree is skewed to one side, the space complexity
    # will be linear. As a result, the space comlexity is O(N).
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        return max(left_height, right_height) + 1
