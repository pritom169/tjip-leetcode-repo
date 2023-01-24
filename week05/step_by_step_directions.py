# TC: O(N + N + N + N) -> O(N), N = number of nodes
# O(N + N) for finding the shortest path from root
# to the nodes.
# Another O(N) for removing the common prefix.
# O(N) again for reversing the strings and adding
# it to the ladder one.

# SC: O(N + N) -> O(N), N = number of nodes
# In the worst case, the tree is skewed to one side and
# to find the distance from root to the node we have to store
# all the direction notations in one array.

# In addition, when the tree is skewed to one side, the
# height of the recursion stack will be N. So it will also 
# be responsible for another O(N) space.

class Solution:
    LEFT = "L"
    RIGHT = "R"
    PARENT = "U"
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # Step 1: Find the path from root to starting node and to destination node.
        # Here, the path will be left and right.
        start = []
        dest = []
        self.find(root, startValue, start)
        self.find(root, destValue, dest)
        
        # Step 2: Now we need to remove the common prefix.
        # For example,if the starting node and destination node
        # exists in the same subtree, and there will be common prefix.
        # if start = LLRL and end = LRL, we need to remove the common 
        # prefix in the beginning. So after removing the prefixes will
        # be start = LRL and end = RL
        while len(start) and len(dest) and start[-1] == dest[-1]:
            start.pop()
            dest.pop()
            
        # Now we need make the first root opposite with by replacing L by U.
        return "".join(self.PARENT * len(start)) + "".join(reversed(dest))
    
    def find(self, node: TreeNode, value: int, path: [str]) -> bool:
        if node.val == value:
            return True
        
        if node.left and self.find(node.left, value, path):
            path.append(self.LEFT)
        elif node.right and self.find(node.right, value, path):
            path.append(self.RIGHT)
        return path
