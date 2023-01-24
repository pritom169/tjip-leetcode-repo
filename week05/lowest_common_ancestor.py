class Solution:
    # TC: O(N), N = Number of nodes.
    # Because we are traversing through each node once.
    
    # SC: O(N), N = Number of nodes.
    # In the best case when the height of the tree is
    # balanced the SC will be O(logN). In the worst case
    # when the tree is skewed to one side the space
    # complexity is O(N).
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return None
        # Step 1: If root equals to any of the nodes, we will not go further
        # into that part of the tree and will return the root, because the
        # node itself can be LCA
        if root == p or root == q: return root
        
        # Step 2: Now we have to search the whole tree.
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # Step 3: We will return the root if both left and 
        # right matches with the respective given nodes. If that
        # is not the case, that means in one of the sides, we have
        # two nodes. Hence, we return the one which matches with one
        # of the nodes.
        return root if (left and right) else left or right
