class Solution:
    # TC: O(N), N = number of nodes
    # Because we are traversing through each node, the time complexity will be
    # O(n)

    # SC: O(N), N = number of nodes
    # The maximum number of nodes at a level is roughly L = (N/2).
    # In the queue, at a time, there could be nodes of two levels.
    # So the maximum size of the queue can be 2 * L = 2 * (N/2) = N
    # Hence, the space complexity will be N
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        
        is_reversed = False
        Q = collections.deque([root])
        zig_zag_list = []

        # The traversing method mentioned below is a classic way of 
        # traversing a Tree in Breadth first manner.  
        while Q:
            Q_Size = len(Q)
            current_level_list = []
            for i in range(Q_Size):
                node = Q.popleft()
                current_level_list.append(node.val)

                if node.left:
                    Q.append(node.left)

                if node.right:
                    Q.append(node.right)
            
            # We are appening the nodes on the basis of flag is_reversed.
            # If the level before is left to right, the current level will be reversed
            # and vise versa.
            zig_zag_list.append(reversed(current_level_list) if is_reversed else current_level_list)
            is_reversed = not is_reversed
        return zig_zag_list
