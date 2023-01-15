class Solution:
    # TC: O(N), N = Total number of values in the nums List.
    # becasue we are traversing to each node once.
    
    # SC: O(logN), N = Number of nodes.
    # Sine the height of the binary tree is balanced the maximum 
    # size of the recusion stack will be logN. That makes the space
    # complexity O(logN).
    
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def distributeNodes(left, right):
            if left > right:
                return
            
            middle = (left + right) // 2
            root = TreeNode(nums[middle])
            root.left = distributeNodes(left, middle - 1)
            root.right = distributeNodes(middle + 1, right)
            return root
        return distributeNodes(0, len(nums) - 1)
