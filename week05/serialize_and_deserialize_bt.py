class Codec:
    # TC: O(N), N = Number of nodes
    # Time complexity for both serialize and deserialize
    # is O(N) because we are traversing through each node.

    # SC: O(N + N + N + N) -> O(N), N = Number of nodes.
    # In both functions we are traversing the tree in Depth
    # first manner. So if the tree is skewed to one side(in
    # the worst case), the space complexity will be O(N + N).

    # In addition, in serialize function we are using additional
    # O(N) space for storing all the values in tree nodes.
    # In the deserialize function, we are also spliting the data
    # and storing the iteratable variables in serialized values.
    # Here the space complexity will be O(N + N)

    # So the total space complexity is O(N + N + N + N) -> O(N)
    def serialize(self, root):
        def goDeeper(node: Optional[TreeNode]):
            if node:
                serialized_string.append(str(node.val))
                goDeeper(node.left)
                goDeeper(node.right)
            else:
                serialized_string.append('#')
        serialized_string = []
        goDeeper(root)
        return " ".join(serialized_string)

    def deserialize(self, data):
        def buildNodes() -> Optional[TreeNode]:
            value = next(serialized_values)
            if value == '#':
                return None
            treeNode = TreeNode(value)
            treeNode.left = buildNodes()
            treeNode.right = buildNodes()
            return treeNode
        serialized_values = iter(data.split())
        return buildNodes()    
