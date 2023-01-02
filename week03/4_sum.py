class Solution:
    #TC: 0(nˆ(k/2)) -> O(nˆ2), K = number of arrays, n = size of the lists
    #SC: O(nˆ(k/2)) -> O(nˆ2), K = number of arrays, n = size of the hashmap, In the worst
    # case every sum count will be one 
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        def compute_sum(lists: List[List[int]]):
            res = collections.Counter({ 0 : 1 })
            for lst in lists:
                temp = collections.Counter()
                for item in lst:
                    for result in res:
                        temp[result + item] += res[result]
                res = temp
            return res
        
        list_array = [nums1, nums2, nums3, nums4]
        k = len(list_array)

        # We are deviding the arrays into two parts.
        left, right = compute_sum(list_array[:k//2]), compute_sum(list_array[k//2:])

        # After getting both side we are multiplying each other
        # by the opposite number.

        # For example: left has -8 -> 2 and right 8 -> 2.
        # Means it must have 4 combnations which makes the
        # result 0.
        return sum(left[s] * right[-s] for s in left)
