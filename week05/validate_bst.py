class Solution:
    # TC: O(n), n = number of nodes in the tree.
    # If it is a valid BST we have to traverse each node to 
    # verify. Hence time complexity will be O(n).

    # SC: O(H), H = Height of the tree.
    # If the height of the binary tree is balanced, H will be logn.
    # In the worst case, the tree will be skewed to one side. Hence,
    # the heght will be n.
    # n = number of nodes in the tree.
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(root)
    
    def isValid(self, root, low = - math.inf, high = math.inf) -> bool:
        if not root: return True

        # If root value satisfies this conditions means, it is not a valid
        # BST
        if (root.val <= low) or (root.val >= high):
            return False
        
        # Now we go the recursively to the left and to the right of the BST,
        # in order to verify the particular node.
        return self.isValid(root.left, low, root.val) and self.isValid(root.right, root.val, high)
