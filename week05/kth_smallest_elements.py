# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # TC: O(H + K), H = Height of the BST.
    # H is n when BST is skewed to one side, and
    # logn when the height is balanced.
    # K = The serial of the smallest value.

    # SC: O(H). H = Height of the BST.
    # The variation of H mentioned in TC also applies here.
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []

        # Keep the loop running until it returns something
        while True:
            # Keep searching to the left as long as it goes
            while root:
                stack.append(root)
                root = root.left
            
            # We will pop the first element in the stack and
            # and assign it as a root.
            root = stack.pop()

            # As we pop one item, we decrease the number.
            k -= 1

            # k == 0, we have found the kth smallest value.
            # Hence, we return the root.
            if k == 0: return root.val

            # If k != 0, means the current value is not value
            # we are looking for so we go to the right and repeat
            # the process again.
            root = root.right
