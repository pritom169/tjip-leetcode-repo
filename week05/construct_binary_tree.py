class Solution:
    # TC: O(N + N) -> O(N), N = Size of both preorder or inorder since both are equal
    # Going through of each element in inorder array will take O(n) time.
    # In the convertToTree function we again are going though again each node in
    # preorder. It will also take O(n) time.

    # SC: O(N + H) -> O(n), N = Size of both preorder or inorder since both are equal.
    # H = Height of the tree

    # Assigning inorder values to a dictionary will take O(N) space.
    # When going through the preorder array, if the height is balanced,
    # H will be logN. If the tree is skewed to one side, H will be N.
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def convertToTree(left, right) -> Optional[TreeNode]:
            if left > right: return None 
            nonlocal preorder_index
            root_value = preorder[preorder_index]
            root = TreeNode(root_value)

            preorder_index += 1

            root.left = convertToTree(left, inorder_index_map[root_value] - 1)
            root.right = convertToTree(inorder_index_map[root_value] + 1, right)
            return root
            
        preorder_index = 0
        inorder_index_map = {}

        for (index, value) in enumerate(inorder):
            inorder_index_map[value] = index
        
        return convertToTree(0, len(inorder) - 1)
