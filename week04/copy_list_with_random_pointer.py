class Solution:
    # TC: O(n + n + n) -> O(3n) -> O(n), because we are traversing the list 3
    # times.

    # SC: O(1). Question might arise, if we are adding additional n number 
    # of nodes to the list why the space complexity is not O(n)?

    # The answer is, regardless what we do, we have to add additional n number
    # of nodes. So we can not consider that into the space complexity. But if we
    # needed more space, for example, if we stored the original values in a hashmap,
    # we would have needed extra O(n) space.
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        # Step 1: Creating a duplicate value and putting it right next to it.
        # For example: Duplicate of A is A'. Putting the duplicate just next
        # to the main, the final list will be like AA'BB'CC'DD'......
        point = head
        while point:
            new_node = Node(point.val, None, None)
            new_node.next = point.next
            point.next = new_node
            point = new_node.next
        
        # Step 2: Assigning the random value from the main one to the copied one.
        # We have to iterate two steps every time, because the copind one is just
        # next to the original one.
        point = head
        while point:
            point.next.random = point.random.next if point.random else None
            point = point.next.next
        
        # Step 3: Original and copied, both linked list are in the same list. Now
        # we have to seperate it.
        old_list = head
        new_list = head.next
        new_head = head.next

        while old_list:
            old_list.next = old_list.next.next
            new_list.next = new_list.next.next if new_list.next else None

            old_list = old_list.next
            new_list = new_list.next
        return new_head
