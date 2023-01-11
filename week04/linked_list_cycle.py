class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # TC: O(N), N = Size of the linked list without cycle lenth
        # There are two time complexities.
        # 1. No cycle: If linked list has no cycle then the maximum
        # amount of iterations is N.
        # 2. Cycle: If it has cycle, in the worst case the the slow
        # pointer will be resonsible for N iterations and fast pointer
        # will be responsible for K amount of iterations.
        # Hence the total time complexity will be O(N+K) which is O(N)

        #SC: O(1), in the Floyd's algorithm we are using constant amount
        # of space.
        if not head: return False

        fast, slow = head.next, head
        while fast != slow:
            if (fast is None) or (fast.next is None):
                return False
            fast = fast.next.next
            slow = slow.next
        return True 
