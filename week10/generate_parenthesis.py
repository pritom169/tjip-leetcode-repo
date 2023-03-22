class Solution:
    # TC: O(2ˆ2N) but it is a upper bound, N = Pairs of parenthesis.
    # SC: O(2ˆ2N) but it is a upper bound, N = Pairs of parenthesis.
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        def back_track(left = 0, right = 0, string = []):
            # Step 1: We check whether it has the current amount
            # of parenthesis or not. If affirmative, we will append
            # it to the result.
            if len(string) == 2 * n:
                answer.append("".join(string))
                return
            # Step 2: The second tip, we will never allow the closing
            # parenthesis to appear first. So if the left parentheses
            # amount is less than n, we can be sure one opeing parentheses
            # can be append.
            if left < n:
                string.append('(')
                back_track(left + 1, right, string)
                string.pop()
            # Step 3: As long as the right parameter is less then left, we
            # keep appending it to the stack.
            if right < left:
                string.append(')')
                back_track(left, right + 1, string)
                string.pop()
        back_track()
        return answer
