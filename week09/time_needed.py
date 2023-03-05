class Solution:
    # TC: O(N + N) -> O(N), N = Number of Employees.
    # First, we are assigning the employees to their manager which
    # has O(N) time complexity.
    # Second, for performing the dfs on the employee tree we also 
    # need O(N) complexity.

    # SC: O(N), N = Number of Employees
    # The maximum size of the map will be O(N).
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        head_map = collections.defaultdict(list)
        # Step 1: We are creating a map, where key is the
        # manager ID and the values are the employess who
        # works for him.
        for (index, manager) in enumerate(manager):
            head_map[manager].append(index)

        # Step 2: We will perform the dfs function from the 
        # headID, and from that will will go deep.
        def dfs(manager):
            result = 0

            for employee in head_map[manager]:
                result = max(dfs(employee) + informTime[manager], result)
            return result
        
        return dfs(headID)
