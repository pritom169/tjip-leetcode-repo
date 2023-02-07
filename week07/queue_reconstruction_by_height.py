class Solution:
    # TC: O(N^2 + NlogN + NlogN) -> O(N^2), N = Number of people in the list
    # Here we are first sorting in decending order for the height that takes
    # O(NlogN) times.
    # Then we are sorting heights on the basis of the counts. Again that is
    # responsible for O(NlogN) times.
    # After that we are inserting at certian position. For inserting an element
    # at a certain position (in the worst case) we have to copy rest of the 
    # elements, put the element in the desired position and then copy rest of
    # the just next to it one by one. It takes total O(N) time complexity and 
    # doing it for N time takes total O(N^2) complexity.

    # SC: O(N), N = Number of people in the list.
    # Because we are storing N elements in the answer array.
    
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x:(-x[0], x[1]))
        answer = []

        for p in people:
            answer.insert(p[1], p)
        return answer
