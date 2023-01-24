class Solution:
    # TC: O(HN), H = Height of the binary tree, N = number of nodes.
    # In the first level we are traversing thorugh N nodes. In the
    # second level we will traverse through (N - N/2)nodes, and so on
    # and so forth. Hence, here the time complexity will be O(N)

    # As just mentioned, in each height level we are traversing thorugh roughly N nodes. If height
    # of the tree is balanced then the total time complexity will be O(Nlogn),
    # if the tree is skewed to one side, the time complexity will be O(Nˆ2)

    # SC: O(N + N), N = Number of nodes.
    # Because we are ultimately returning all the nodes, that will be responsible
    # for O(N) time complexity.
    # Also recursion stack will also be responsible for O(N) in the worst
    # case(when the tree is skewed).
    # So the total time complexity will be O(N + N) -> O(N)
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        
        all_leaves = []
        while root:
            current_level_leaves = []
            root = self.removeLeaves(root, current_level_leaves)
            all_leaves.append(current_level_leaves)
        return all_leaves
    
    def removeLeaves(self, root: Optional[TreeNode], current_level_leaves: List[int]) -> Optional[TreeNode]:
        if not root:
            return None
        if (root.left is None) and (root.right is None):
            current_level_leaves.append(root.val)
            return None
        root.left = self.removeLeaves(root.left, current_level_leaves)
        root.right = self.removeLeaves(root.right, current_level_leaves)
        return root
