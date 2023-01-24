class Solution:
    # TC: O(N), N = Number of nodes
    # We are traversing through each node once, so the time
    # complexity will be O(N).

    # SC: O(N), N = Number of nodes
    # If the height of the binary tree is balanced, the space
    # complexity will be O(logN), if the Tree is skewed to one
    # side, the space complexity will be O(N). So the actual
    # space complexity is O(N).
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = -math.inf
        
        def findMaxPath(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            nonlocal max_sum

            # The main intuition of solving the problem is we will
            # calculate the sum of all the subtrees and store it in
            # the max_sum value, but when we are done calculating the sum
            # we will just return the max value of the left or right
            # path, so that the immediate parent node can also simulate
            # a path.

            # Here we have to take the maximum values between 0 and the value,
            # because the node itself can be a path. If all the child nodes
            # has negative values and current node has positive, we can filter them
            # in this way.
            max_from_left = max(findMaxPath(node.left), 0)
            max_from_right = max(findMaxPath(node.right), 0)
            max_sum = max(max_sum, max_from_left + node.val + max_from_right)

            return max(node.val + max_from_left, node.val + max_from_right)
        findMaxPath(root)
        return max_sum
