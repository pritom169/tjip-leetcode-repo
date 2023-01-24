class Solution:
    # TC: O(N), N = number of nodes.
    # We are traversing thorugh each node once.
    
    # SC: O(N), N = number of nodes.
    # As usual in the case of a binary tree, in the
    # best case the height will be balanced and the 
    # space complexity will be O(logN). On the contrary,
    # in the worst case, the height of the tree will be
    # linear and the space complexity will be O(N). So
    # the actual time complexity is O(N).
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isMirror(root.left, root.right) if root is not None else None
    
    def isMirror(self, left, right):
        if left is None and right is None:
            return True
        
        if left is None or right is None:
            return False
        
        if left.val == right.val:
            outerPair = self.isMirror(left.left, right.right)
            innerPair = self.isMirror(left.right, right.left)
            return outerPair and innerPair
        else:
            return False
