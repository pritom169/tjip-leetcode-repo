class Solution:
    # TC: O(max(m,n)) m = lenth of l1, n = lenth of l2
    # SC: O(max(m,n)) m = lenth of l1, n = lenth of l2
    # At worst the max lenth could be max(m,n) + 1
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(0)
        current = dummyNode
        carry = 0

        # We have to go through as long as one of the is non-empty.
        # We may have to go one more iteration because of the carry.
        while l1 != None or l2 != None or carry != 0:
            l1value = l1.val if l1 else 0
            l2value = l2.val if l2 else 0
            column_sum = l1value + l2value + carry
            carry = (column_sum) // 10
            next_node = ListNode(column_sum % 10)
            current.next = next_node
            current = next_node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummyNode.next
