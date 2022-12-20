class Solution:
    # TC: O(2 * filtered_S + |s| + |t|) -> O(|s| + |t|) -> S = size of s and T = size of t
    # SC: O(|s| + |t|) -> S = size of s and T = size of t

    def minWindow(self, s: str, t: str) -> str:
        # A dictionary is needed to keep the counts of all the unique characters
        char_counts = collections.Counter(t)

        # Number of unique characters required in the window.
        required = len(char_counts)

        # We are taking a filtered arrays of tuples. In this array we will store
        # the character present in t from s with the index.
        filtered_s = []
        for index, char in enumerate(s):
            if char in char_counts:
                filtered_s.append((index, char))
        
        # Number of unique characters present in the window
        window_char = 0

        # Character counts in the current window.
        window_counts = {}

        right, left = 0 ,0
        answer = (float("inf"), left, right)

        while right < len(filtered_s):
            # As we go forward we keep the character counts of the current window.
            char = filtered_s[right][1]
            window_counts[char] = window_counts.get(char, 0) + 1

            # If the charter count in the current window matches t, we increase the
            # unique char count.
            if window_counts[char] == char_counts[char]:
                window_char += 1
            
            # As long as the current window has all the characters from t, we will try
            # to shrink the window.
            while (left <= right) and (window_char == required):
                char = filtered_s[left][1]

                start = filtered_s[left][0]
                end = filtered_s[right][0]
                # If this current window has the smallest lenth, we store the start and
                # the end of the window.
                if (end - start + 1) < answer[0]:
                    answer = ((end - start + 1), start, end)
                
                # As we are moving forward we need to reduce the left character count by one.
                window_counts[char] -= 1

                # After reducing the count if current window has less character count than in
                # t, we will have reduce the counter of uniruw characters.
                if window_counts[char] < char_counts[char]:
                    window_char -= 1
                
                left += 1
            right += 1
        
        return "" if answer[0] == float("inf") else s[answer[1]: answer[2] + 1]
