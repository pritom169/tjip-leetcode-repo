# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # TC: O(n), n = number of nodes
    # SC: O(1) because we are not storing any values.
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # This is the iterative way of solving the problem
        previous = None
        current = head

        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        return previous
