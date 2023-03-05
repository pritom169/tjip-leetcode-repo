class Solution:
    # TC: O(|P| + |C|), P = Number of prerequisites, C = Number of total courses
    # In the first part, we have gone through every prerequisites which account
    # for O(P) complexity.
    # On the second part, when we check whether cycle exists or not, in the worst
    # case, it will check every course which in the end constitutes for O(|P| + |C|)
    # complexity.

    # SC: O(|P| + |C|), P = Number of prerequisites, C = Number of total courses
    # First we are creating the map for the prerequisites which will take O(|P| + |C|)
    # complexity. 
    # Second, we are creating two flag arrays to keep track of the cycle and also
    # finishing the vertices. It constitutes of O(2.|C|) complexity.
    # Third, it order to check the cycle the postorder DFS recusion stack will have O
    # (|C|) complexity. 
    # Totally, it will have O(|P| + 4.|C|) complexity or O(|P| + |C|) space complexity.
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Step 1: First we need to declare a dictionary to store
        # if one course is done, which course can be done next.
        
        course_map = collections.defaultdict(list)
        for (course, prerequisite) in prerequisites:
            course_map[prerequisite].append(course)
        
        cycle_flag   = [False] * numCourses
        checked_flag = [False] * numCourses

        # Step 2: We go thorugh every course and check it has a 
        # cycle or not.
        for curr_course in range(numCourses):
            if self.is_cycle(curr_course, course_map, cycle_flag, checked_flag):
                return False
        return True
    
    def is_cycle(self, curr_course, course_map, cycle_flag, checked_flag):
        # To find a cycle we have to go though some steps. Since it is recursive
        # function we have to declare some base topic.

        # Step 1: We are checking if the course has already been checked. If it is
        # True, that means we are sure there are no cycle.
        if checked_flag[curr_course]: return False
        # Step 2: If we find this True, that means during the cycle do exists.
        if cycle_flag[curr_course]: return True

        # Step 3: As we are visiting we are making the flag True
        cycle_flag[curr_course] = True
        result = False

        # Step 4: For every course that we can do, we have to recusively check
        # whether a cycle exists or not.
        for course in course_map[curr_course]:
            result = self.is_cycle(course, course_map, cycle_flag, checked_flag)
            if result: break
        
        # Step 5: After we are done checking, we change both flags
        cycle_flag[curr_course] = False
        checked_flag[curr_course] = True
        return result
