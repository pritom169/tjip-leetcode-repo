# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # TC: O(NlogK), N = total number of nodes in all the linked lists, 
    # K = number of levels.
    # What is level?
    # For example, that are total 8 sorted lists. We are going from 8 sorted lists to
    # 8 -> 4 -> 2 -> 1 label. So, log(8) = 3

    # SC: O(1), as the input size increases we still use constant space.
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists and len(lists) == 0:
            return
        
        while (len(lists) > 1):
            mergedLists = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i+1] if i+1 < len(lists) else None
                mergedLists.append(self.mergeTwoLists(list1, list2))
            lists = mergedLists
        return lists[0]
        
    def mergeTwoLists(self, list1, list2):
        head = point = ListNode(0)
        while list1 and list2:
            if list1.val < list2.val:
                point.next = list1
                list1 = list1.next
            else:
                point.next = list2
                list2 = list2.next
            point = point.next
        
        if list1:
            point.next = list1
        if list2:
            point.next = list2
        return head.next
