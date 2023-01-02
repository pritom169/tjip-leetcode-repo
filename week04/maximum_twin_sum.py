# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # TC: O(n), n = size of the node
    # SC: O(1), we are using constant space.
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast, slow = head, head
        max_value = 0

        # Getting to the half of the linked list
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        curr, prev = slow, None

        # Reversing the second part of the list
        while curr:
            prev, curr.next, curr = curr, prev, curr.next 
        
        # Now going through both of the list and storing the max value.
        while prev:
            max_value = max(max_value, head.val + prev.val)
            head = head.next
            prev = prev.next
        return max_value
