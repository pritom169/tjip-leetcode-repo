class Solution:
    # TC: O(n), n = The number of total nodes, because we travel each node once.
    # SC: O(1), we are not using any extra spaces as input size increases.
    
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
       current, nextNode = root, root.left if root else None
       while current and nextNode:
           # Step 1: Point to the next node who has the same parent.
           current.left.next = current.right

           # Step 2: If next node exists, connect the two next nodes who
           # has different parents.
           if current.next:
               current.right.next = current.next.left
            
            # Step 3: Move the current pointer to the right.
           current = current.next

           # Step 4: If current is None, that means we have traversed
           # one level of the tree. Now we traverse the tree in the next level.
           if not current:
                current = nextNode
                nextNode = current.left
       return root
