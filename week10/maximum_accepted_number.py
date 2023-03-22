class Solution:
    # TC: O(N*M), N = Number of boys, M = Number of girls
    # Because we are traveling every cell possible.

    # SC: O(N + N*M) -> O(N*M), N = Number of boys, M = Number of girls
    # We need O(N) space for N amount of keys in the matches.
    # We need another O(N*M) space in the worst case for the recursion stack. 
    def maximumInvitations(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        matches_map = {}

        def back_tracking(boy, visited: set()):
            for girl in range(N):
                if grid[boy][girl] and girl not in visited:
                    visited.add(girl)

                    # Step 1: The guy will ask a girl. If she says
                    # yes, that will be it.

                    # Step 2: If the girl is already taken, and another
                    # guy wants to take that girl, the girl has to ask
                    # her previous partner to find another girl. If the
                    # past partner finds another girl, only then she
                    # can go with the new partner.
                    
                    if girl not in matches_map or back_tracking(matches_map[girl], visited): 
                        matches_map[girl] = boy
                        return True
            return False
        
        for boy in range(M):
            back_tracking(boy, set())
        return len(matches_map)
