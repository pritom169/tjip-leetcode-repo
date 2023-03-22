class Solution:
    # TC: O(N), N = Number of items in the preorder array
    # SC: O(1), because we are using constant space.
    def verifyPreorder(self, preorder: List[int]) -> bool:
        smallest = -math.inf
        i = 0
        for item in preorder:
            if item < smallest: return False
            while i > 0 and item > preorder[i-1]:
                smallest = preorder[i-1]
                i -= 1
            preorder[i] = item
            i += 1
        return True 
