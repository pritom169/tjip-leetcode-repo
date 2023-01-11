# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # TC: O(1), since we are not iterating through the linked list, it is constant time
    # SC: O(1), we are using a constant extra space
    def deleteNode(self, node):
        # A temporary value is needed to be stored somewhere
        next_node = node.next

        # Update the current node value with the value of the next node
        node.val = next_node.val

        # Now we set the next node reference with the next_node.next node reference
        node.next = next_node.next

        # Since the next node is seperated from the current node, we delete the next reference
        next_node.next = None

        # For safety, we are deleting the temporary vairiable
        del(next_node)
