class Solution:
    # TC: O(N), N = number of nodes
    # Since, we are traversing through each node, hence the
    # time complexity will be O(N)

    # SC: O(N), N = number of nodes
    # The maximum size of queue will entirely depend on the
    # maximum number of elements in one level. As a result,
    # the space complexity will be O(N)
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        # In the first step, the root will be in the queue
        Q = collections.deque([root])
        while Q:
            # The queue will run until it is empty, which indicates
            # we have traversed every node in the tree.
            queue_size = len(Q)
            for i in range(queue_size):
                # The node we will pop will be the left most node,
                # because we will go from left to right. 
                node = Q.popleft()

                # If this conditions fulfils, means there is another
                # node, next to the current node. So we assign our 
                # next pointer to the leftmost element of the queue.
                if i < queue_size - 1:
                    node.next = Q[0]
                
                if node.left:
                    Q.append(node.left)

                if node.right:
                    Q.append(node.right)
        return root
