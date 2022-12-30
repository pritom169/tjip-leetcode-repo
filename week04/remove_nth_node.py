class Solution:
    #TC: O(L), L = Lenth of the linked list
    #SC: O(1)
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # We will use two pointers
        first, second = head, head

        # We will take the first pointer n steps ahead
        for _ in range(n):
            first = first.next
        
        # In some case, n = size of the linked list.
        # For example, head = [1], n = 1, in that case we just
        # return head.next which is empty
        if not first:
            return head.next

        # Now we take two pointers ahead as long as first is not null.
        while first.next:
            first, second = first.next, second.next
        second.next = second.next.next
        return head
