class Solution():
    # TC: O(N + N) -> O(N), N = Number of employees
    # Putting every employee to the information on the basis
    # of the id takes O(N) time.
    # After that, searching for importace against any employee
    # id takes O(N) complexity, in the worst case.

    # SC: O(N + N) -> O(N), N = Number of employees
    # The employee map will take O(N) space.
    # In addition, the recursion stack for doing
    # the dfs will take another O(N) time complexity
    # in the worst case.
    def getImportance(self, employees, query_id):
        employee_map = {}
        def dfs(employee_id):
            employee = employee_map[employee_id]
            importance = employee.importance
            for subordinate in employee.subordinates:
                importance += dfs(subordinate)
            return importance

        for employee in employees:
            employee_map[employee.id] = employee
        return dfs(query_id)
