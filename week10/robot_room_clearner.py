class Solution:
    # TC: O(V-C), V = Number of vertices, C = Number of obstacles.
    # Because we will just travers the empty spaces.
    # SC: O(V-C), V = Number of vertices, C = Number of obstacles.
    # The recursion stack will be maximum of size of empty stacks.      
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        # Step 1: First step we need to write a proper function
        # going back. When it goes one steps back we have to make
        # sure the direction has to be the same. It means he has to
        # turn 360 degrees. Hence, we have to utilize the turnRight
        # function four times. 
        def goBack():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
        
        def back_tracking(cell = (0, 0), d = 0):
            visited.add(cell)
            robot.clean()
            # Step 2: When we finally came to a cell, we have to make sure
            # it has been cleaned, and try to clean the next four adjacent
            # cells.
            for i in range(4):
                new_d = (i + d) % 4
                new_cell = (cell[0] + direction[new_d][0], cell[1] + direction[new_d][1])

                # Step 3: If it is not visited and or can move, continue the backtarcking.
                if (new_cell not in visited) and robot.move():
                    back_tracking(new_cell, new_d)
                    # Step 4: Once, it has been tracked, it needs to go back.
                    goBack()
                robot.turnRight()
        direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()
        back_tracking()
